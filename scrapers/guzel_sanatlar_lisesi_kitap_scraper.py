from scrapers.base_scraper import BaseScraper
from typing import Dict
from bs4 import BeautifulSoup
import queue
from scrapers.helpers import scrape_flibooks

class GuzelSanatlarLisesiKitapScraper(BaseScraper):
    PATH = 'etkilesimli-kitap/guzel-sanatlar-lisesi'
    FILE_HEADERS = [
        "sinifPath", "sinifIsmi", "dersPath", "dersIsmi",
        "flipbookKitapLink", "pdfIndirmeLink", "zipIndirmeLink", "kitapThumbnailLink"
    ]

    def __init__(self):
        super().__init__()
        self.links: queue.Queue[Dict[str, str]] = queue.Queue()

    def scrape(self):
        main_page: BeautifulSoup = self.get_soup_from_url(f"{self.BASE_URL}/{self.PATH}")
        if not main_page:
            return

        self.collect_links(main_page, is_ders=True)

        while not self.links.empty():
            link_info = self.links.get()
            self.process_link(link_info)

    def process_link(self, link_info: Dict[str, str]):
        url = link_info['link_2_scrape']
        del link_info['link_2_scrape']

        page: BeautifulSoup = self.get_soup_from_url(url)
        if not page:
            return
        
        further_contents = page.select('.books-detail-box .books-detail-content')
        if further_contents:
            self.collect_links(page, is_ders=False, defaults=link_info)
        else:
            self.process_books(page, link_info)

    def collect_links(self, page: BeautifulSoup, is_ders=True, defaults=None):
        contents = page.select('.books-detail-box .books-detail-content')
        if not contents:
            return
        
        for content in contents:
            a_tag = content.select_one('a')
            path = a_tag['href'].split('/')[-1]
            if '?' in path:
                path = path.split('?')[0]

            name = a_tag.select_one('.books-detail-head h4').text.strip()
    
            if is_ders:
                new_link_info = {
                                'sinifPath': '', 'sinifIsmi': '',
                                'dersPath': path, 'dersIsmi': name,
                                'link_2_scrape': f"{self.BASE_URL}{a_tag['href']}"}
            else:
                # scraping sinif.
                new_link_info = {'link_2_scrape': f"{self.BASE_URL}{a_tag['href']}",
                                'sinifPath':path, 'sinifIsmi': name,
                                 'dersPath': defaults['dersPath'], 'dersIsmi': defaults['dersIsmi']}
            
            self.links.put(new_link_info)

    def process_books(self, page: BeautifulSoup, link_info: Dict[str, str]):
        scraped_books = scrape_flibooks(page, check_redirect_links=False)
        rows = []
        
        for book in scraped_books:
            rows.append([self.clean_text(item)
                   for item in 
                   [link_info['sinifPath'], link_info['sinifIsmi'],
                    link_info['dersPath'], link_info['dersIsmi']]]
                    + list(book.values()))

        self.write_to_csv(rows)