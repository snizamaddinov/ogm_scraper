from scrapers.books_with_filtering_base_scraper import BooksWithFilteringBaseScraper

__all__ = [
    'KavramOgrenimiEtkilesimliKitapScraper',
    'KazanimKavramaEtkinlikScraper',
    'CalismaDefterScraper',
    'BeceriTemelliEtkilesimliKitaplarScraper'
]


class KavramOgrenimiEtkilesimliKitapScraper(BooksWithFilteringBaseScraper):
    PATH = '/kavram-ogretimi-sec'
    BOOK_PATH = '/kavram-ogretimi'
    FILE_PREFIX = 'Kavram_Ogretimi_Calisma_Kitaplari'


class KazanimKavramaEtkinlikScraper(BooksWithFilteringBaseScraper):
    PATH = '/kazanim-kavrama-sec'
    BOOK_PATH = '/kazanim-kavrama-etkinlik'
    FILE_PREFIX = 'Kazanim_Kavrama_Etkinlikleri'


class CalismaDefterScraper(BooksWithFilteringBaseScraper):
    PATH = '/calisma-defteri-sec'
    BOOK_PATH = '/calisma-defteri'
    FILE_PREFIX = 'Calisma_Defterleri'


class BeceriTemelliEtkilesimliKitaplarScraper(BooksWithFilteringBaseScraper):
    PATH = '/beceri-temelli-kitap-sec'
    BOOK_PATH = '/beceri-temelli-kitap'
    FILE_PREFIX = 'Beceri_Temelli_Etkilesimli_Kitaplar'