from scrapers.kazanim_kavrama_etkinlik_scraper import KazanimKavramaEtkinlikScraper

class KavramOgrenimiEtkilesimliKitapScraper(KazanimKavramaEtkinlikScraper):
    PATH = '/kavram-ogretimi-sec'
    BOOK_PATH = '/kavram-ogretimi'
    FILE_PREFIX = 'Kavram_Ogretimi_Calisma_Kitaplari'
    FILE_HEADERS = [
        "sinifId", "sinifIsmi", "dersId", "dersNo", "dersKodu", "dersIsmi",
        "interaktifKitapLink", "pdfIndirmeLink", "zipIndirmeLink", "kitapThumbnailLink"
    ]

    def scrape(self):
        super().scrape()