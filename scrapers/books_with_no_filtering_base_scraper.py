from scrapers.base_scraper import BaseScraper
from scrapers.helpers import scrape_flibooks


class BooksWithNoFilteringBaseScraper(BaseScraper):
    PATH = ''
    FILE_HEADERS = ["flipbookKitapLink", "pdfIndirmeLink", "zipIndirmeLink", "kitapThumbnailLink"]

    def __init__(self, check_redirect_links: bool):
        super().__init__()
        self.check_redirect_links = check_redirect_links

    def scrape(self):
        html = self.get_soup_from_url(f"{self.BASE_URL}{self.PATH}")
        if not html:
            return
        
        scraped_books = scrape_flibooks(html, check_redirect_links=self.check_redirect_links, domain=self.BASE_URL)
        rows = []
        
        for book in scraped_books:
            rows.append(list(book.values()))

        self.write_to_csv(rows)