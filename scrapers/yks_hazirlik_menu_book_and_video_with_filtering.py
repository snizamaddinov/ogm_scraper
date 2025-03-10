from scrapers.books_and_video_with_filtering_base_scraper import BooksAndVideoWithFilteringBaseScraper

__all__ = ['YksKonuAnlatimlariVideoScraper']


class YksKonuAnlatimlariVideoScraper(BooksAndVideoWithFilteringBaseScraper):
    PATH = '/yks-konu-anlatim'
    FILE_NAME_PREFIX = 'Yks_Konu_Anlatimlari_Video'

