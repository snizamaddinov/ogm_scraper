from scrapers.pdf_links_with_filtering_base_scraper import PdfLinksWithFilteringBaseScraper

__all__ = [
    'KazanimBazliKazanimKavramaEtkinlikScraper',
    'KazanimBazliKavramOgrenimiEtkilesimliKitapScraper',
    'KazanimBazliBeceriTemelliEtkinlikKitapScraper'
]


class KazanimBazliKazanimKavramaEtkinlikScraper(PdfLinksWithFilteringBaseScraper):
    PATH = '/kazanim-kavrama-kazanim-liste'
    FILE_NAME_PREFIX = 'Kazanim_Bazli_Kazanim_Kavrama_Etkinlik'
    PDF_DOWNLOAD_PATH = '/panel/upload/yardimci-kitap/'


class KazanimBazliKavramOgrenimiEtkilesimliKitapScraper(PdfLinksWithFilteringBaseScraper):
    PATH = '/kavram-ogretimi-kazanim-liste'
    FILE_NAME_PREFIX = 'Kazanim_Bazli_Kavram_Ogretimi_Calisma_Kitaplari'
    PDF_DOWNLOAD_PATH = '/panel/upload/yardimci-kitap/'


class KazanimBazliBeceriTemelliEtkinlikKitapScraper(PdfLinksWithFilteringBaseScraper):
    PATH = '/beceri-temelli-kazanim'
    FILE_NAME_PREFIX = 'Kazanim_Bazli_Beceri_Temelli_Etkinlik_Kitaplari'
    PDF_DOWNLOAD_PATH = '/panel/upload/yardimci-kitap/'