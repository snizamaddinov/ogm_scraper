from typing import Set, Tuple
from abc import ABCMeta, abstractmethod
import pathlib
from scrapers.base_scraper import BaseScraper
import csv
import os
from requests.adapters import HTTPAdapter, Retry
import requests
from urllib import parse

class BaseDownloader(metaclass=ABCMeta):
    DATA_FOLDER = 'downloaded_pdf_files'

    def __init__(self):
        self.processed_rows: Set = set()
        self.current_row: dict = dict()
        self.session = requests.Session()
        retries = Retry(total=5, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
        self.session.mount("https://", HTTPAdapter(max_retries=retries))

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
        file_name = self.get_output_filename()
        final_path = os.path.join(relative_path, file_name)

        path = pathlib.Path(relative_path)
        path.mkdir(parents=True, exist_ok=True)

        return final_path

    def is_processed_row(self):
        current_row_final_path = self.get_final_path()
        result = current_row_final_path in self.processed_rows
        return result

    def download(self):
        for download_link, file_name in self.unique_row_generator():
            if os.path.exists(file_name):
                self.processed_rows.add(file_name)
                continue

            try:
                with self.session.get(download_link, stream=True, timeout=10) as response:
                    if response.status_code == 200:

                        with open(file_name, 'wb') as file:
                            for chunk in response.iter_content(chunk_size=1024):
                                if chunk:
                                    file.write(chunk)

                        print(f"Downloaded: {file_name}")
                        self.processed_rows.add(file_name)
                    else:
                        print(f"Failed to download {download_link}: {response.status_code}")

            except requests.RequestException as e:
                print(f"Failed to download {download_link}: {e}")


class ScraperClassDownloader(BaseDownloader, metaclass=ABCMeta):
    SCRAPER_CLASS: BaseScraper

    def __init__(self):
        super().__init__()
        self.current_processed_file = None
        self.classes_to_scrape: list[BaseScraper] = self.get_classes_to_scrape()
        self.file_name_prefixes: list[str] = self.get_file_name_prefixes()

        self.source_data_path: pathlib.Path = self.get_data_path()
        self.destination_data_path: pathlib.Path = self.get_data_path(source=False)

        self.processed_files = set()
        self.current_processed_file_prefix = None

    def get_classes_to_scrape(self):
        return self.SCRAPER_CLASS.__subclasses__()

    def get_relative_path(self, extras: list[str] = None) -> str:
        if not extras:
            extras = []

        path = os.path.join(self.destination_data_path, self.current_processed_file_prefix, *extras)

        return path

    def is_valid_row(self)-> bool:
        if not self.current_row:
            return False

        if not self.get_download_link():
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
        for file_name_prefix in self.file_name_prefixes:
            if not file_name_prefix in self.processed_files:
                files = self.source_data_path.glob(f"{file_name_prefix}_*.csv")
                files = sorted(files, key=lambda x: x.stat().st_mtime)

                if files:
                    yield file_name_prefix, files[-1].absolute()


    def unique_row_generator(self):
        file_names = self.file_name_generator()
        for prefix, file_name in file_names:
            self.current_processed_file_prefix = prefix
            self.processed_files.add(prefix)

            with open(file_name, 'r', encoding='utf-8-sig') as f:
                reader = csv.DictReader(f)
                for row in reader:

                    self.current_row = row
                    if self.is_valid_row() and not self.is_processed_row():
                        yield self.get_download_link(), self.get_final_path()


class ScraperVideoDownloader(ScraperClassDownloader):
    DATA_FOLDER = 'downloaded_video_files'
    SCRAPER_CLASS = BaseScraper
    YOUTUBE_DOMAINS = ['youtube.com', 'youtu.be']

    def is_valid_row(self) -> bool:
        if not super().is_valid_row():
            return False

        link = self.get_download_link()

        parsed = parse.urlparse(link)
        if any([domain in parsed.netloc for domain in self.YOUTUBE_DOMAINS]):
            return False

        return True

    def get_download_link(self) -> str:
        return self.current_row['videoLink']

    def get_output_filename(self) -> str:
        unique_id = self.current_row['videoId']
        if '.mp4' not in unique_id:
            unique_id = f"{unique_id}.mp4"

        return unique_id
