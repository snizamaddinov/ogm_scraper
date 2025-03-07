from scrapers.base_scraper import BaseScraper
from bs4 import BeautifulSoup
from scrapers.helpers import scrape_flibooks


class SporLisesiKitapScraper(BaseScraper):
    PATH = '/etkilesimli-kitap/spor-lisesi'
    FILE_HEADERS = ["flipbookKitapLink", "pdfIndirmeLink", "zipIndirmeLink", "kitapThumbnailLink"]
    FILE_NAME_PREFIX = 'Spor_Lisesi_Kitaplari'

    def __init__(self):
        super().__init__()
        self.check_redirect_links = False

    def scrape(self):
        html = self.get_soup_from_url(f"{self.BASE_URL}{self.PATH}")
        if not html:
            return
        
        scraped_books = scrape_flibooks(html, check_redirect_links=self.check_redirect_links, domain=self.BASE_URL)
        rows = []
        
        for book in scraped_books:
            rows.append(list(book.values()))

        self.write_to_csv(rows)