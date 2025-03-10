from scrapers.books_with_filtering_base_scraper import BooksWithFilteringBaseScraper

class BeceriTemelliEtkilesimliKitaplarScraper(BooksWithFilteringBaseScraper):
    PATH = '/beceri-temelli-kitap-sec'
    BOOK_PATH = '/beceri-temelli-kitap'
    FILE_PREFIX = 'Beceri_Temelli_Etkilesimli_Kitaplar'