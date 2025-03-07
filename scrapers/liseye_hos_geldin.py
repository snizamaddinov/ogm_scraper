from scrapers.spor_lisesi_kitap_scraper import SporLisesiKitapScraper


class LiseyeHosGeldinScraper(SporLisesiKitapScraper):
    PATH = '/liseye-hosgeldin'
    FILE_NAME_PREFIX = 'Liseye_Hosgeldin_Kitaplari'

    def __init__(self):
        super().__init__()
        self.check_redirect_links = True

