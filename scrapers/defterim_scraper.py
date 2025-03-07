from scrapers.guzel_sanatlar_lisesi_kitap_scraper import GuzelSanatlarLisesiKitapScraper

class DefterimScraper(GuzelSanatlarLisesiKitapScraper):
    PATH = '/defterim'
    FILE_NAME_PREFIX = 'Defterim_Kitaplari'

    def __init__(self):
        super().__init__()
        self.is_initial_ders = False
        self.check_redirect_links = True
