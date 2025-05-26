import os
import importlib
import pkgutil
from downloaders import helpers
from scrapers.books_and_video_with_filtering_base_scraper import BooksAndVideoWithFilteringBaseScraper
from scrapers.books_and_video_no_filtering_base_scraper import BookAndVideoNoFilteringBaseScraper
from scrapers.video_scraper import VideoScraper
from downloaders.base_downloader import ScraperVideoDownloader

_submodules_imported = False

def import_submodules(package_name):
    global _submodules_imported
    if _submodules_imported:
        return

    package = importlib.import_module(package_name)
    package_path = os.path.dirname(package.__file__)

    for _, module_name, _ in pkgutil.iter_modules([package_path]):
        importlib.import_module(f"{package_name}.{module_name}")

    _submodules_imported = True

import_submodules("scrapers")


class BooksAndVideoNoFilteringVideoDownloader(ScraperVideoDownloader):
    SCRAPER_CLASS = BooksAndVideoWithFilteringBaseScraper


class BooksAndVideoWithFilteringVideoDownloader(ScraperVideoDownloader):
    SCRAPER_CLASS = BookAndVideoNoFilteringBaseScraper


class VideoDownloader(ScraperVideoDownloader):
    SCRAPER_CLASS = VideoScraper

    def get_download_link(self) -> str:
        link = self.current_row.get('videoLink', '')
        if '.mp4_1.mp4' in link:
            link = link.replace('.mp4_1.mp4', '_1.mp4')

        return link

    def get_relative_path(self, extras: list[str] = None) -> str:
        grade_name = helpers.format_folder_name(self.current_row.get('sinifIsmi', 'unknown_grade'))
        subject_code = helpers.format_folder_name(self.current_row.get('dersKod', 'unknown_subject'))

        return super().get_relative_path(extras=[grade_name, subject_code])

    def get_old_relative_path(self, extras: list[str] = None) -> str:
        grade_name = helpers.format_folder_name(self.current_row.get('sinifIsmi', 'unknown_grade'))
        subject_code = helpers.format_folder_name(self.current_row.get('dersKod', 'unknown_subject'))
        chapter_name = helpers.format_folder_name(self.current_row.get("uniteIsmi", 'unknown_chapter'))
        gain_name = helpers.format_folder_name(self.current_row.get('kazanimIsmi', 'unknown_gain'))

        return super().get_relative_path(extras=[grade_name, subject_code, chapter_name, gain_name])

    def get_old_output_filename(self) -> str:
        video_name = helpers.format_folder_name(self.current_row.get('videoBaslik', ''))
        video_id = self.current_row.get('videoId')
        if '.mp4' in video_id:
            video_id.replace('.mp4', '')

        return f"{video_id}__{video_name}.mp4"
