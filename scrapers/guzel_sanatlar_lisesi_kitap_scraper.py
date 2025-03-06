from scrapers.base_scraper import BaseScraper
from typing import Dict
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
        self.links: queue.Queue[Dict[str, str]] = queue.Queue()

    def scrape(self):
        main_page: BeautifulSoup = self.get_soup_from_url(f"{self.BASE_URL}/{self.PATH}")
        if not main_page:
            return

        self.collect_links(main_page, is_ders=False)

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
            self.collect_links(page, is_ders=True, defaults=link_info)
        else:
            self.scrape_book_details(page, link_info)

    def collect_links(self, page: BeautifulSoup, is_ders=True, defaults=None):
        contents = page.select('.books-detail-box .books-detail-content')
        if not contents:
            return
        
        for content in contents:
            a_tag = content.select_one('a')
            path = a_tag['href'].split('/')[-1]
            name = a_tag.select_one('.books-detail-head h4').text.strip()
    
            if is_ders:
                new_link_info = defaults.copy()
                new_link_info.update({'dersPath': path, 'dersIsmi': name,
                                      'link_2_scrape': f"{self.BASE_URL}{a_tag['href']}"})
            else:
                new_link_info = {'link_2_scrape': f"{self.BASE_URL}{a_tag['href']}",
                                'sinifPath':path, 'sinifIsmi': name, 'dersPath': '', 'dersIsmi': ''}
            
            self.links.put(new_link_info)

    def scrape_book_details(self, page: BeautifulSoup, link_info: Dict[str, str]):
        books = page.select('.books-detail-action-content')
        rows = []

        for book in books:
            flipbook_link = ''  
            pdf_link = ''
            zip_link = ''
            thumbnail_link = book.select_one('img')['src']

            for action_link in book.select('.books-detail-action-buttons a'):
                href = action_link['href']

                if href.endswith('.html'):
                    flipbook_link = href
                elif href.endswith('.pdf'):
                    pdf_link = href
                elif href.endswith('.zip'):
                    zip_link = href

            row = [self.clean_text(item)
                   for item in 
                   [link_info['sinifPath'], link_info['sinifIsmi'],
                    link_info['dersPath'], link_info['dersIsmi'],
                    flipbook_link, pdf_link, zip_link, thumbnail_link]
            ]

            rows.append(row)

        self.write_to_csv(rows)