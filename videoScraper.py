import requests
import re
import time
import csv
import os
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

FILENAME ='video_data.csv'
FILE_HEADERS = ["sinifId", "sinifIsmi", "dersId", "dersNo", "dersIsmi", "uniteId", "uniteNo", "uniteIsmi", "kazanimId", "kazanimNo", "kazanimKod", "kazanimIsmi", 'videoId', 'videoBaslik', 'videoLink']
PATTERNS = {
    'apostrophe': r"[\u2019\u2018\u2032\u0060\u00B4\u02BC\u02BB\u02BD\u0022\u201C\u201D\u201E\u2033\u2036\u275D]",
    'whitespace': r"[\n\r\t]",
    'multiple_spaces': r"\s{2,}",
    'kazanim_code': r'^[\w.İŞĞÜÇÖıüşğöç]+(?:[\d.İŞĞÜÇÖıüşğöç]*)?\s*-?',
    'video_id': r"videoGoster\('([^']+)"
}

COMPILED_PATTERNS = {key: re.compile(value) for key, value in PATTERNS.items()}

def clean_text(text):
    if not text:
        return ""
    text = COMPILED_PATTERNS['apostrophe'].sub("'", text)
    text = COMPILED_PATTERNS['whitespace'].sub(" ", text)
    text = COMPILED_PATTERNS['multiple_spaces'].sub(" ", text)
    return text.strip()

def get_kazanim_code(kazanim_ismi):
    match = re.match(COMPILED_PATTERNS['kazanim_code'], kazanim_ismi.strip())
    return match.group(0).strip(" -") if match else ""

def exponential_backoff_request(url, method="GET", data=None, max_retries=5):
    wait_time = 4
    for _ in range(max_retries):
        try:
            response = requests.request(method, url, headers=HEADERS, json=data)
            if response.status_code == 200:
                return response.json() if method == "POST" else response.text
        except requests.exceptions.RequestException:
            print("Request failed. Retrying with exponential backoff...: ", wait_time)
            time.sleep(wait_time)
            wait_time *= 2

    return None

def get_initial_data():
    # get html from Default.aspx
    html = exponential_backoff_request("https://ogmmateryal.eba.gov.tr/ebatv-ogm/Default.aspx", "GET")
    return html


def get_grade_options(html):
    soup = BeautifulSoup(html, "html.parser")
    options = soup.select("#dlSinif option")
    grade_list = []
    for opt in options:
        sinif_id = opt.get("value", "").strip()
        sinif_name = opt.text.strip()
        if sinif_id and sinif_id != "0":
            grade_list.append((sinif_id, sinif_name))
    return grade_list
def parse_id_array_from_script(script_text, function_name):
    # Looks for something like: function dersSil() { ... var dids = [8,7,44,...]; ... }
    # We'll capture the numbers in the array
    # function_name in ["dersSil", "uniteSil", "kazanimSil"]
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

def parse_ders_unite_kazanim_ids(html):
    scripts = re.findall(r"<script[^>]*>(.*?)</script>", html, re.DOTALL)
    target_script = scripts[-1]
    ders_ids, unite_ids, kazanim_ids = set(), set(), set()
    
    if "function dersSil" in target_script:
        ders_ids = parse_id_array_from_script(target_script, "dersSil")

    if "function uniteSil" in target_script:
        unite_ids = parse_id_array_from_script(target_script, "uniteSil")

    if "function kazanimSil" in target_script:
        kazanim_ids = parse_id_array_from_script(target_script, "kazanimSil")

    return ders_ids, unite_ids, kazanim_ids


def get_ders_list(sinif_id):
    return exponential_backoff_request(f"https://ogmmateryal.eba.gov.tr/api/ders-listele/{sinif_id}", "POST") or []

def get_unite_list(ders_id):
    print(f"{' '*2}Getting unit list for subject:", ders_id)
    data = exponential_backoff_request(f"https://ogmmateryal.eba.gov.tr/api/unite-listele/{ders_id}", "POST")
    if not data:
        return [{"id": 0, "baslik": ""}]
    print(f"{' '*2}Total number of units: :", len(data))
    return data

def get_kazanim_list(unite_id):
    print(f"{' '*3}Getting outcome list for unit:", unite_id)
    data = exponential_backoff_request(f"https://ogmmateryal.eba.gov.tr/api/kazanim-listele/{unite_id}", "POST")
    if not data:
        return [{"id": 0, "baslik": ""}]
    
    print(f"{' '*3}Total number of outcomes: :", len(data))
    return data

def get_video_items(sinif_id, ders_id, unite_id, kazanim_id):
    url_page = f"https://ogmmateryal.eba.gov.tr/ebatv-ogm/VideoListele.aspx?s={sinif_id}&d={ders_id}&u={unite_id}&k={kazanim_id}"
    html_page = exponential_backoff_request(url_page, "GET")
    if not html_page:
        return []
    soup = BeautifulSoup(html_page, "lxml")
    items = soup.select("div.sidebar-content-item a")
    return items

def write_to_csv(rows):
    file_exists = os.path.isfile(FILENAME)

    with open(FILENAME, 'a', encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(FILE_HEADERS)
        
        writer.writerows(rows)

def scrape_data():
    html = get_initial_data()

    ders_ids_set, unite_ids_set, kazanim_ids_set = parse_ders_unite_kazanim_ids(html)
    grade_options = get_grade_options(html)

    for sinif_id, sinif_name in grade_options:
        ders_list = get_ders_list(sinif_id)
        print("Now scraping for grade:", sinif_name)
        print("Total number of subjects:", len(ders_list))
        for ders in ders_list:
            if ders_ids_set and ders.get("id", 0) not in ders_ids_set:
                continue

            ders_id, ders_no, ders_name = ders.get("id", 0), ders.get('sire', 0), ders.get("baslik", "")

            unite_list = get_unite_list(ders_id)
            print(f"{' '*2}Total number of units for subject:", len(unite_list))
            for unite in unite_list:
                if unite_ids_set and unite.get("id", 0) not in unite_ids_set:
                    continue

                unite_id, unite_no, unite_name = unite.get("id", 0), unite.get('sira', 0), unite.get("baslik", "")

                kazanim_list = get_kazanim_list(unite_id)
                print(f"{' '*3}Total number of outcomes for unit:", len(kazanim_list))
                rows_to_write = []
                for kazanim in kazanim_list:
                    if kazanim_ids_set and kazanim.get("id", 0) not in kazanim_ids_set:
                        continue

                    kazanim_id, kazanim_no, kazanim_name = kazanim.get("id", 0), kazanim.get('sira', 0), kazanim.get("baslik", "")
                    kazanim_code = get_kazanim_code(kazanim_name)

                    items = get_video_items(sinif_id, ders_id, unite_id, kazanim_id)
                    for a in items:
                        video_baslik = clean_text(a.get_text())
                        onclick_attr = a.get("onclick", "")
                        match = re.search(COMPILED_PATTERNS['video_id'], onclick_attr)
                        if match:
                            video_id = clean_text(match.group(1))
                            # According to the JS, they replace ".mp4" with "_1.mp4" for the final URL
                            video_id_for_link = video_id.replace(".mp4", "_1.mp4")
                            video_link = f"https://ogmmateryal.eba.gov.tr/ebatv-ogm/upload/uzev-480/{video_id_for_link}"
                            rows_to_write.append([
                                sinif_id,
                                clean_text(sinif_name),
                                ders_id,
                                ders_no,
                                clean_text(ders_name),
                                unite_id,
                                unite_no,
                                clean_text(unite_name),
                                kazanim_id,
                                kazanim_no,
                                kazanim_code,
                                clean_text(kazanim_name),
                                video_id,
                                video_baslik,
                                video_link
                            ])
                    
                if rows_to_write:
                    print(f"{' '*3}Writing length of rows:", len(rows_to_write))
                    write_to_csv(rows_to_write)
                else:
                    
                    print(f"{' '*3}No videos found for unit:", unite_name)
                    print(f"{' '*3}Subject:", ders_name)
                    print(f"{' '*3}Grade:", sinif_name)
                    

scrape_data()
