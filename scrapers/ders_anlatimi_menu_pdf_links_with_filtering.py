from scrapers.pdf_links_with_filtering_base_scraper import PdfLinksWithFilteringBaseScraper


__all__ = [
    'DersAnlatimSunulariScraper',
    'KonuOzetleriScraper'
]


class KonuOzetleriScraper(PdfLinksWithFilteringBaseScraper):
    PATH = '/konu-ozetleri'
    FILE_NAME_PREFIX = 'Konu_Ozetleri'
    PDF_DOWNLOAD_PATH = '/panel/upload/fasikul/'


class DersAnlatimSunulariScraper(PdfLinksWithFilteringBaseScraper):
    PATH = '/ders-sunulari'
    FILE_NAME_PREFIX = 'Ders_Anlatim_Sunumlari'
    PDF_DOWNLOAD_PATH = '/panel/upload/files/'