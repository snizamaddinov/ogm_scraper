from scrapers.flip_book_with_grade_scraper_base import FlipBookWithGradeScraperBase

class OyunVeEtkinliklerScraper(FlipBookWithGradeScraperBase):
    PATH = '/oyun-etkinlik'
    FILE_NAME_PREFIX = 'Oyun_Ve_Etkinlik_Kitaplari'

    def __init__(self):
        super().__init__(is_initial_ders=True, check_redirect_links=False)