from scrapers.books_with_no_filtering_base_scraper import BooksWithNoFilteringBaseScraper


class LiseyeHosGeldinScraper(BooksWithNoFilteringBaseScraper):
    PATH = '/liseye-hosgeldin'
    FILE_NAME_PREFIX = 'Liseye_Hosgeldin_Kitaplari'

    def __init__(self):
        super().__init__(check_redirect_links=True)

