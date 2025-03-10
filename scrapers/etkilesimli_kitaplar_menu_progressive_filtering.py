from scrapers.books_with_progressive_filtering_base_scraper import BooksWithProgressiveFilteringBaseScraper

class GuzelSanatlarLisesiKitapScraper(BooksWithProgressiveFilteringBaseScraper):
    PATH = '/etkilesimli-kitap/guzel-sanatlar-lisesi'
    FILE_NAME_PREFIX = 'Guzel_Sanatlar_Lisesi_Kitaplari'

    def __init__(self):
        super().__init__(is_initial_ders=True, check_redirect_links=False)


class OyunVeEtkinliklerScraper(BooksWithProgressiveFilteringBaseScraper):
    PATH = '/oyun-etkinlik'
    FILE_NAME_PREFIX = 'Oyun_Ve_Etkinlik_Kitaplari'

    def __init__(self):
        super().__init__(is_initial_ders=True, check_redirect_links=False)


class DefterimScraper(BooksWithProgressiveFilteringBaseScraper):
    PATH = '/defterim'
    FILE_NAME_PREFIX = 'Defterim_Kitaplari'

    def __init__(self):
        super().__init__(is_initial_ders=False, check_redirect_links=True)