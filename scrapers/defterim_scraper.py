from scrapers.books_with_progressive_filtering_base_scraper import BooksWithProgressiveFilteringBaseScraper

class DefterimScraper(BooksWithProgressiveFilteringBaseScraper):
    PATH = '/defterim'
    FILE_NAME_PREFIX = 'Defterim_Kitaplari'

    def __init__(self):
        super().__init__(is_initial_ders=False, check_redirect_links=True)
