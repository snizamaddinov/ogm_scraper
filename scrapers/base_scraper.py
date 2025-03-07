import requests
import re
import time
import csv
import os
import string
import pathlib
from bs4 import BeautifulSoup
from typing import List, Dict, Any, Optional, Tuple

class BaseScraper:
    BASE_URL = "https://ogmmateryal.eba.gov.tr"
    HEADERS = {"User-Agent": "Mozilla/5.0"}
    DATA_FOLDER = 'data' #TODO take from env

    def __init__(self):
        self.compiled_patterns = {
            'apostrophe': re.compile(r"[\u2019\u2018\u2032\u0060\u00B4\u02BC\u02BB\u02BD\u0022\u201C\u201D\u201E\u2033\u2036\u275D]"),
            'whitespace': re.compile(r"[\n\r\t]"),
            'multiple_spaces': re.compile(r"\s{2,}"),
            'kazanim_code': re.compile(r'^[\w.İŞĞÜÇÖıüşğöç]+(?:[\d.İŞĞÜÇÖıüşğöç]*)?\s*-?'),
            'script_tag': re.compile(r"<script[^>]*>(.*?)</script>", re.DOTALL)
        }

        self.FILE_NAME = self.construct_clean_filename_from_title()
        
        self.FILE_PATH = self.construct_file_path()

        print(f"File name: {self.FILE_NAME}")
        print(f"File path: {self.FILE_PATH}")
        # exit()
    
    def construct_clean_filename_from_title(self)->str:
        if hasattr(self, "FILE_NAME_PREFIX"):
            return f"{self.FILE_NAME_PREFIX}_{time.strftime('%Y%m%d_%H%M%S')}.csv"

        url = f"{self.BASE_URL}{self.PATH if self.PATH.startswith('/') else f'/{self.PATH}'}"
        print("URL: ", url)
        self.base_html = self.exponential_backoff_request(url)
        soup = BeautifulSoup(self.base_html, "lxml")
        title = soup.title.string
        main = title.split("|")[0].strip()
    
        # turkish letters to english
        turkish = "çğıöşü"
        english = "cgiosu"
        tr_to_eng = str.maketrans(turkish, english)
        main = main.lower().translate(tr_to_eng).replace("(", "").replace(")", "")
        segments = [string.capwords(segment) for segment in main.split(" ")]
        filename = "_".join(segments)

        return f"{filename}_{time.strftime('%Y%m%d_%H%M%S')}.csv"

    def construct_file_path(self):
        current_path = pathlib.Path(__file__).parent.absolute()
        parent_path = current_path.parent
        data_path = parent_path / self.DATA_FOLDER
        data_path.mkdir(exist_ok=True)
        file_path = data_path / self.FILE_NAME
        return file_path
    
    def clean_text(self, text: str) -> str:
        if not text:
            return ""
        text = self.compiled_patterns['apostrophe'].sub("'", text)
        text = self.compiled_patterns['whitespace'].sub(" ", text)
        text = self.compiled_patterns['multiple_spaces'].sub(" ", text)
        return text.strip()

    def get_kazanim_code(self, kazanim_ismi: str) -> str:
        match = self.compiled_patterns['kazanim_code'].match(kazanim_ismi.strip())
        return match.group(0).strip(" -") if match else ""

    def exponential_backoff_request(self, url: str, method: str = "GET", 
                                  data: Optional[Dict] = None, max_retries: int = 5) -> Optional[Any]:
        wait_time = 4
        for _ in range(max_retries):
            try:
                response = requests.request(method, url, headers=self.HEADERS, json=data)
                if response.status_code == 200:
                    return response.json() if method == "POST" else response.text
            except requests.exceptions.RequestException as e:
                print(f"Request failed: {e}")
                print(f"Request failed. Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
                wait_time *= 2
        return None

    def get_soup_from_url(self, url: str) -> Optional[BeautifulSoup]:
        html = self.exponential_backoff_request(url)
        if not html:
            return None
        return BeautifulSoup(html, "lxml")

    def fetch_grades(self, html: str=None) -> List[Tuple[str, str]]:
        if not html:
            url = f"{self.BASE_URL}{self.PATH if self.PATH.startswith('/') else f'/{self.PATH}'}"
            html = self.exponential_backoff_request(url)

        if not html:
            return []
        
        if isinstance(html, BeautifulSoup):
            soup = html
        else:
            soup = BeautifulSoup(html, "lxml")
    
        return [(opt["value"], opt.text.strip()) 
                for opt in soup.select("select#dlSinif option[value]") 
                if opt["value"] != "0"]

    def write_to_csv(self, rows: List[List[str]]):
        file_exists = os.path.isfile(self.FILE_PATH)
        
        with open(self.FILE_PATH, 'a', encoding="utf-8-sig", newline="") as f:
            writer = csv.writer(f)
            if not file_exists and self.FILE_HEADERS:
                writer.writerow(self.FILE_HEADERS)
            writer.writerows(rows)
    
    def get_last_line(self)-> Optional[dict]:
        with open(self.FILE_NAME, "rb") as f:
            try:
                f.seek(-2, os.SEEK_END)
                while f.read(1) != b'\n':
                    f.seek(-2, os.SEEK_CUR)

            except OSError:
                return None

            last_line = f.readline().decode().strip()
            header = ','.join(self.FILE_HEADERS)

            if last_line == header:
                return None
            
            last_line_dict = dict(zip(self.FILE_HEADERS, last_line.split(",")))
            return last_line_dict

    def get_subject_list(self, sinif_id: str) -> List[Dict]:
        return self.exponential_backoff_request(f"{self.BASE_URL}/api/ders-listele/{sinif_id}", "POST") or []

    def get_unit_list(self, ders_id: int) -> List[Dict]:
        return self.exponential_backoff_request(f"{self.BASE_URL}/api/unite-listele/{ders_id}", "POST") or []

    def get_kazanim_list(self, unite_id: int) -> List[Dict]:
        gains = self.exponential_backoff_request(f"{self.BASE_URL}/api/kazanim-listele/{unite_id}", "POST") or []
        for gain in gains:
            gain["kod"] = self.get_kazanim_code(gain["baslik"])

        return gains
    
    def scrape(self):
        raise NotImplementedError("Subclasses must implement scrape method") 
    
    def parse_id_array_from_script(self, script_text, function_name):
        pattern = rf"{function_name}\s*\(\)\s*{{.*?var dids\s*=\s*\[([^\]]*)\];.*?}}"

        match = re.search(pattern, script_text, re.DOTALL)
        if not match:
            return set()
        raw_ids = match.group(1)

        ids = set()
        for x in raw_ids.split(","):
            x = x.strip()
            if x.isdigit():
                ids.add(int(x))
        return ids

    def parse_ders_unite_kazanim_ids(self, html):
        scripts = re.findall(self.compiled_patterns['script_tag'], html)
        target_script = scripts[-1]
        ders_ids, unite_ids, kazanim_ids = set(), set(), set()
        
        if "function dersSil" in target_script:
            ders_ids = self.parse_id_array_from_script(target_script, "dersSil")

        if "function uniteSil" in target_script:
            unite_ids = self.parse_id_array_from_script(target_script, "uniteSil")

        if "function kazanimSil" in target_script:
            kazanim_ids = self.parse_id_array_from_script(target_script, "kazanimSil")

        return ders_ids, unite_ids, kazanim_ids