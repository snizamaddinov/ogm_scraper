from scrapers.base_scraper import BaseScraper
from typing import List, Dict
from bs4 import BeautifulSoup
import queue

class GuzelSanatlarLisesiKitapScraper(BaseScraper):
    PATH = 'etkilesimli-kitap/guzel-sanatlar-lisesi'
    FILE_HEADERS = [
        "sinifPath", "sinifIsmi", "dersPath", "dersIsmi",
        "flipbookKitapLink", "pdfIndirmeLink", "zipIndirmeLink", "kitapThumbnailLink"
    ]

    def __init__(self):
        super().__init__()
        self.links: queue[dict[str, str]] = queue.Queue()

    def scrape(self):
        main_page: BeautifulSoup = self.get_soup_from_url(f"{self.BASE_URL}/{self.PATH}")
        if not main_page:
            return
        
        

        pass
        