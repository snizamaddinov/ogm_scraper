from selenium.webdriver.support.expected_conditions import none_of

from downloaders.base_downloader import ScraperClassDownloader
from scrapers.books_with_no_filtering_base_scraper import BooksWithNoFilteringBaseScraper
from scrapers.books_with_filtering_base_scraper import BooksWithFilteringBaseScraper
from scrapers.books_with_progressive_filtering_base_scraper import BooksWithProgressiveFilteringBaseScraper
from scrapers.books_and_video_with_filtering_base_scraper import BooksAndVideoWithFilteringBaseScraper
from scrapers.books_and_video_no_filtering_base_scraper import BookAndVideoNoFilteringBaseScraper
from scrapers.pdf_links_with_filtering_base_scraper import PdfLinksWithFilteringBaseScraper
from scrapers.interactive_books_scraper import InteractiveBooksScraper

import os
import importlib
import pkgutil
from downloaders import helpers

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



class BooksAndVideoNoFilteringDownloader(ScraperClassDownloader):
    scraper_class = BookAndVideoNoFilteringBaseScraper

    def get_download_link(self) -> str:
        return self.current_row['pdfLink']

    def get_output_filename(self) -> str:
        unique_id = self.current_row['pdfId']
        if '.pdf' not in unique_id:
            unique_id = f"{unique_id}.pdf"

        return unique_id


class BooksAndVideoWithFilteringDownloader(ScraperClassDownloader):
    scraper_class = BooksAndVideoWithFilteringBaseScraper

    def get_download_link(self) -> str:
        return self.current_row['pdfLink']

    def get_output_filename(self) -> str:
        unique_id = self.current_row['pdfId']
        if '.pdf' not in unique_id:
            unique_id = f"{unique_id}.pdf"

        return unique_id

    def get_relative_path(self, *args, **kwargs) -> str:
        ders_kodu = helpers.format_folder_name(kwargs['dersKodu'])
        sinav_tipi = helpers.format_folder_name(kwargs['sinavTipi'])

        return super().get_relative_path(extras=[ders_kodu, sinav_tipi])


class BooksWithFilteringDownloader(ScraperClassDownloader):
    scraper_class = BooksWithFilteringBaseScraper
    static_url_part = 'http://ogmmateryal.eba.gov.tr/panel/upload/etkilesimli/kitap'

    def get_download_link(self) -> str:
        return self.current_row['pdfIndirmeLink']

    def get_output_filename(self) -> str:
        file_name = helpers.format_filename_from_url(self.get_download_link(), self.static_url_part)
        if '.pdf' not in file_name:
            file_name = f"{file_name}.pdf"

        return file_name

    def get_relative_path(self, *args, **kwargs) -> str:
        grade_name = helpers.format_folder_name(self.current_row['sinifIsmi'])
        subject_name = helpers.format_folder_name(self.current_row['dersIsmi'])

        return super().get_relative_path(extras=[grade_name, subject_name])


class BooksWithNoFilteringDownloader(ScraperClassDownloader):
    scraper_class = BooksWithNoFilteringBaseScraper

    def get_download_link(self) -> str:
        link =  self.current_row['pdfIndirmeLink']
        if not link:
            link = self.current_row['flipbookKitapLink']

        return link

    def get_output_filename(self) -> str:
        file_name = helpers.format_filename_from_url(self.get_download_link())
        if '.pdf' not in file_name:
            file_name = f"{file_name}.pdf"

        return file_name


class BooksWithProgressiveFilteringDownloader(ScraperClassDownloader):
    scraper_class = BooksWithProgressiveFilteringBaseScraper

    def get_download_link(self) -> str:
        return self.current_row['pdfIndirmeLink']

    def get_output_filename(self) -> str:
        file_name = helpers.format_filename_from_url(self.get_download_link())
        if '.pdf' not in file_name:
            file_name = f"{file_name}.pdf"

        return file_name

    def get_relative_path(self, *args, **kwargs) -> str:
        grade_name = helpers.format_folder_name(self.current_row['sinifIsmi'])
        subject_name = helpers.format_folder_name(self.current_row['dersIsmi'])

        return super().get_relative_path(extras=[grade_name, subject_name])


class PdfLinksWithFilteringDownloader(ScraperClassDownloader):
    scraper_class = PdfLinksWithFilteringBaseScraper

    def get_download_link(self) -> str:
        return self.current_row['pdfLink']

    def get_output_filename(self) -> str:
        unique_id = self.current_row['pdfId']
        if '.pdf' not in unique_id:
            unique_id = f"{unique_id}.pdf"

        print("output file name: ", unique_id)
        return unique_id

    def get_relative_path(self, *args, **kwargs) -> str:
        grade_name = helpers.format_folder_name(self.current_row['sinifIsmi'])
        subject_name = helpers.format_folder_name(self.current_row['dersIsmi'])

        return super().get_relative_path(extras=[grade_name, subject_name])


class DersKitaplariDownloader(ScraperClassDownloader):
    scraper_class = InteractiveBooksScraper

    def get_classes_to_scrape(self):
        return [InteractiveBooksScraper]

    def get_download_link(self) -> str:
        return self.current_row['pdfIndirmeLink']

    def get_output_filename(self) -> str:
        unique_id = self.current_row['kitapId']
        if '.pdf' not in unique_id:
            unique_id = f"{unique_id}.pdf"

        return unique_id

    def get_relative_path(self, *args, **kwargs) -> str:
        grade_name = helpers.format_folder_name(self.current_row['sinifIsmi'])
        subject_name = helpers.format_folder_name(self.current_row['dersIsmi'])

        return super().get_relative_path(extras=[grade_name, subject_name])


class BooksAndVideoNoFilteringVideoDownloader(ScraperClassDownloader):
    scraper_class = InteractiveBooksScraper

    def get_download_link(self) -> str:
        pass