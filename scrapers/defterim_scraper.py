from scrapers.flip_book_with_grade_scraper_base import FlipBookWithGradeScraperBase

class DefterimScraper(FlipBookWithGradeScraperBase):
    PATH = '/defterim'
    FILE_NAME_PREFIX = 'Defterim_Kitaplari'

    def __init__(self):
        super().__init__(is_initial_ders=False, check_redirect_links=True)
