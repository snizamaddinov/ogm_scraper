from scrapers.books_with_progressive_filtering_base_scraper import BooksWithProgressiveFilteringBaseScraper

class OyunVeEtkinliklerScraper(BooksWithProgressiveFilteringBaseScraper):
    PATH = '/oyun-etkinlik'
    FILE_NAME_PREFIX = 'Oyun_Ve_Etkinlik_Kitaplari'

    def __init__(self):
        super().__init__(is_initial_ders=True, check_redirect_links=False)