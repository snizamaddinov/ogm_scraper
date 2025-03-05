from base_scraper import BaseScraper
import re
from bs4 import BeautifulSoup

class VideoScraper(BaseScraper):
    FILE_NAME = 'video_data.csv'
    FILE_HEADERS = [
        "sinifId", "sinifIsmi", "dersId", "dersNo", "dersIsmi", "uniteId", "uniteNo", "uniteIsmi",
        "kazanimId", "kazanimNo", "kazanimKod", "kazanimIsmi", 'videoId', 'videoBaslik', 'videoLink'
    ]

    def __init__(self):
        super().__init__()
        self.compiled_patterns['video_id'] = re.compile(r"videoGoster\('([^']+)")

    def get_initial_data(self):
        return self.exponential_backoff_request(f"{self.BASE_URL}/ebatv-ogm/Default.aspx", "GET")

    def get_video_items(self, sinif_id: str, ders_id: int, unite_id: int, kazanim_id: int):
        url_page = f"{self.BASE_URL}/ebatv-ogm/VideoListele.aspx?s={sinif_id}&d={ders_id}&u={unite_id}&k={kazanim_id}"
        html_page = self.exponential_backoff_request(url_page)
        if not html_page:
            return []
        soup = BeautifulSoup(html_page, "lxml")
        return soup.select("div.sidebar-content-item a")

    def scrape(self):
        html = self.get_initial_data()
        grade_options = self.fetch_grades()
        # Rest of your video scraping implementation... 