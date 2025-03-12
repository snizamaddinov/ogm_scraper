from typing import Set, Tuple
from abc import ABCMeta, abstractmethod
import pathlib
from .helpers import request_with_backoff
from scrapers.base_scraper import BaseScraper
import csv
import os

class BaseDownloader(metaclass=ABCMeta):
    DATA_FOLDER = 'downloaded_data'
    def __init__(self):
        self.processed_rows: Set = set()
        self.current_row: dict = dict()

    @abstractmethod
    def get_download_link(self) -> str:
        pass

    @abstractmethod
    def get_relative_path(self) -> str:
        pass

    @abstractmethod
    def get_output_filename(self) -> str:
        pass

    @abstractmethod
    def unique_row_generator(self)-> Tuple[str, str]:
        pass

    def get_final_path(self) -> str:
        relative_path = self.get_relative_path()
        print("Accepted relative path: ", relative_path)
        file_name = self.get_output_filename()
        print("Accepted file name: ", file_name)
        final_path = os.path.join(relative_path, file_name)
        print("Final name2: ", final_path)

        path = pathlib.Path(relative_path)
        path.mkdir(parents=True, exist_ok=True)

        print("Final path is created: ", final_path)
        return final_path

    def is_processed_row(self):
        current_row_final_path = self.get_final_path()
        return current_row_final_path in self.processed_rows

    def download(self):
        for download_link, file_name in self.unique_row_generator():
            if not os.path.exists(file_name):
                response = request_with_backoff(download_link)
                with open(file_name, 'wb') as file:
                    file.write(response.content)
            self.processed_rows.add(file_name)


class ScraperClassDownloader(BaseDownloader, metaclass=ABCMeta):
    scraper_class: BaseScraper

    def __init__(self):
        super().__init__()
        self.current_processed_file = None
        self.classes_to_scrape: list[BaseScraper] = self.get_classes_to_scrape()
        print("Classes to scrape: ", self.classes_to_scrape)
        # exit()
        self.file_name_prefixes: list[str] = self.get_file_name_prefixes()

        self.source_data_path: pathlib.Path = self.get_data_path()
        self.destination_data_path: pathlib.Path = self.get_data_path(source=False)

        self.processed_files = set()
        self.current_processed_file_prefix = None

    def get_classes_to_scrape(self):
        return self.scraper_class.__subclasses__()

    def get_relative_path(self, extras: list[str] = None) -> str:
        if not extras:
            extras = []

        path = os.path.join(self.destination_data_path, self.current_processed_file_prefix, *extras)
        print("path44: ", path)

        return path

    def is_valid_row(self)-> bool:
        if not self.current_row:
            return False

        return True

    def get_file_name_prefixes(self):
        prefixes = []
        for class_ in self.classes_to_scrape:
            if hasattr(class_, 'FILE_NAME_PREFIX'):
                prefixes.append(class_.FILE_NAME_PREFIX)

        return prefixes

    def get_data_path(self, source=True)-> pathlib.Path:
        current_path = pathlib.Path(__file__).parent.absolute()
        parent_path = current_path.parent
        if source:
            data_path = parent_path / BaseScraper.DATA_FOLDER
        else:
            data_path = parent_path / self.DATA_FOLDER

        return data_path

    def file_name_generator(self):
        print("file_name_generator")
        print("file_name_prefixes: ", self.file_name_prefixes)
        for file_name_prefix in self.file_name_prefixes:
            if not file_name_prefix in self.processed_files:
                files = self.source_data_path.glob(f"{file_name_prefix}_*.csv")
                files = sorted(files, key=lambda x: x.stat().st_mtime)

                if files:
                    yield file_name_prefix, files[-1].absolute()


    def unique_row_generator(self):
        print("Unique row generator")
        print("Counter: 0")
        file_names = self.file_name_generator()
        for prefix, file_name in file_names:
            count = 0
            self.current_processed_file_prefix = prefix
            self.processed_files.add(prefix)

            with open(file_name, 'r', encoding='utf-8-sig') as f:
                reader = csv.DictReader(f)
                for row in reader:

                    self.current_row = row
                    if self.is_valid_row() and not self.is_processed_row():
                        print("Processing row: ", count)
                        count += 1
                        yield self.get_download_link(), self.get_final_path()
                        if count > 1:
                            print("Breaking..")
                            break