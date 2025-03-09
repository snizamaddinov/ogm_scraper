from scrapers.flip_book_with_grade_scraper_base import FlipBookWithGradeScraperBase

class GuzelSanatlarLisesiKitapScraper(FlipBookWithGradeScraperBase):
    PATH = '/etkilesimli-kitap/guzel-sanatlar-lisesi'
    FILE_NAME_PREFIX = 'Guzel_Sanatlar_Lisesi_Kitaplari'

    def __init__(self):
        super().__init__(is_initial_ders=True, check_redirect_links=False)
