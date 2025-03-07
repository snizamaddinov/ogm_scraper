from scrapers.kazanim_bazli_kazanim_kavrama_etkinlik_scraper import KazanimBazliKazanimKavramaEtkinlikScraper

class KazanimBazliKavramOgrenimiEtkilesimliKitapScraper(KazanimBazliKazanimKavramaEtkinlikScraper):
    PATH = '/kavram-ogretimi-kazanim-liste'
    BOOK_PATH = '/kavram-ogretimi-kazanim-liste'
    FILE_NAME_PREFIX = 'Kazanim_Bazli_Kavram_Ogretimi_Calisma_Kitaplari'