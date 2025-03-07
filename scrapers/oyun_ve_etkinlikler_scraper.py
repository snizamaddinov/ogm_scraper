from scrapers.guzel_sanatlar_lisesi_kitap_scraper import GuzelSanatlarLisesiKitapScraper

class OyunVeEtkinliklerScraper(GuzelSanatlarLisesiKitapScraper):
    PATH = 'oyun-etkinlik'
    FILE_NAME_PREFIX = 'Oyun_Ve_Etkinlik_Kitaplari'