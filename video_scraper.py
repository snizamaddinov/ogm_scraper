from base_scraper import BaseScraper
import re
from bs4 import BeautifulSoup

class VideoScraper(BaseScraper):
    PATH = '/ebatv-ogm/Default.aspx'
    FILE_HEADERS = [
        "sinifId", "sinifIsmi", "dersId", "dersNo", "dersKod", "dersIsmi", "uniteId", "uniteNo", "uniteIsmi",
        "kazanimId", "kazanimNo", "kazanimKod", "kazanimIsmi", 'videoId', 'videoBaslik', 'videoLink'
    ]
    VIDEO_DOWNLOAD_LINK = "https://ogmmateryal.eba.gov.tr/ebatv-ogm/upload/uzev-480/{video_id_for_link}"

    def __init__(self):
        super().__init__()
        self.compiled_patterns['video_id'] = re.compile(r"videoGoster\('([^']+)")
        self.compiled_patterns['script_tag'] = re.compile(r"<script[^>]*>(.*?)</script>", re.DOTALL)

    def get_initial_data(self):
        return self.exponential_backoff_request(f"{self.BASE_URL}{self.PATH}", "GET")

    def get_video_items(self, sinif_id: str, ders_id: int, unite_id: int, kazanim_id: int):
        url_page = f"{self.BASE_URL}/ebatv-ogm/VideoListele.aspx?s={sinif_id}&d={ders_id}&u={unite_id}&k={kazanim_id}"
        html_page = self.exponential_backoff_request(url_page)
        if not html_page:
            return []
        soup = BeautifulSoup(html_page, "lxml")
        return soup.select("div.sidebar-content-item a")

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
    def scrape(self):
        html = self.get_initial_data()

        ders_ids_set, unite_ids_set, kazanim_ids_set = self.parse_ders_unite_kazanim_ids(html)
        grade_options = self.fetch_grades(html)

        for grade_id, grade_name in grade_options:
            subjects = self.get_subject_list(grade_id)

            for subject in subjects:
                if ders_ids_set and subject["id"] not in ders_ids_set:
                    continue

                chapters = self.get_unit_list(subject["id"])
                for chapter in chapters:
                    if unite_ids_set and chapter["id"] not in unite_ids_set:
                        continue
                    
                    file_rows = []
                    gains = self.get_kazanim_list(chapter["id"])
                    for gain in gains:
                        if kazanim_ids_set and gain["id"] not in kazanim_ids_set:
                            continue

                        video_items = self.get_video_items(grade_id, subject["id"], chapter["id"], gain["id"])
                        for video in video_items:
                            onclick_attr = video.get("onclick", "")
                            video_id = self.compiled_patterns['video_id'].search(onclick_attr)
                            if not video_id:
                                continue
                            video_title = self.clean_text(video.get_text())
                            video_id = self.clean_text(video_id.group(1))
                            # According to the JS, they replace ".mp4" with "_1.mp4" for the final URL
                            video_id_for_link = video_id.replace(".mp4", "_1.mp4")
                            video_link = self.VIDEO_DOWNLOAD_LINK.format(video_id_for_link=video_id_for_link)
                            row = [ self.clean_text(item) if isinstance(item, str) else item
                                for item in
                                [grade_id, grade_name, subject["id"], subject["sira"], subject['kod'], subject["baslik"],
                                chapter["id"], chapter["sira"], chapter["baslik"], gain["id"], gain["sira"],
                                gain["kod"], gain["baslik"], video_id, video_title, video_link]
                            ]

                            file_rows.append(row)

                    self.write_to_csv(file_rows)