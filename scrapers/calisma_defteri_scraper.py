from scrapers.books_with_filtering_base_scraper import BooksWithFilteringBaseScraper

class CalismaDefterScraper(BooksWithFilteringBaseScraper):
    PATH = '/calisma-defteri-sec'
    BOOK_PATH = '/calisma-defteri'
    FILE_PREFIX = 'Calisma_Defterleri'