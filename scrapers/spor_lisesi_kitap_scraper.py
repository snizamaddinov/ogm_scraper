from scrapers.books_with_no_filtering_base_scraper import  BooksWithNoFilteringBaseScraper


class SporLisesiKitapScraper(BooksWithNoFilteringBaseScraper):
    PATH = '/etkilesimli-kitap/spor-lisesi'
    FILE_NAME_PREFIX = 'Spor_Lisesi_Kitaplari'

    def __init__(self):
        super().__init__(check_redirect_links=False)