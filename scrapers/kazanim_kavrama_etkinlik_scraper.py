from scrapers.base_scraper import BaseScraper
from scrapers.helpers import scrape_flibooks
from scrapers.books_with_filtering_base_scraper import BooksWithFilteringBaseScraper

class KazanimKavramaEtkinlikScraper(BooksWithFilteringBaseScraper):
    PATH = '/kazanim-kavrama-sec'
    BOOK_PATH = '/kazanim-kavrama-etkinlik'
    FILE_PREFIX = 'Kazanim_Kavrama_Etkinlikleri'