from scrapers.books_with_filtering_base_scraper import BooksWithFilteringBaseScraper

class KavramOgrenimiEtkilesimliKitapScraper(BooksWithFilteringBaseScraper):
    PATH = '/kavram-ogretimi-sec'
    BOOK_PATH = '/kavram-ogretimi'
    FILE_PREFIX = 'Kavram_Ogretimi_Calisma_Kitaplari'