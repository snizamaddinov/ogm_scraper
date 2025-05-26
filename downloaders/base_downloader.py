import logging
from typing import Set, Tuple
from abc import ABCMeta, abstractmethod
import pathlib
from scrapers.base_scraper import BaseScraper
import csv
import os
from requests.adapters import HTTPAdapter, Retry
import requests
from urllib import parse
from datetime import datetime
import re
import hashlib
import traceback
from pathlib import Path


class Logger(logging.Logger):
    PATH = 'logs/downloaders'

    def __init__(self, name, level=logging.NOTSET):
        super().__init__(name, level)

        path = pathlib.Path(self.PATH)
        path.mkdir(parents=True, exist_ok=True)
        log_file = path / f"{name}.log"

        self.setLevel(level)
        handler = logging.FileHandler(log_file)
        handler.setLevel(level)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.addHandler(handler)

class BaseDownloader(metaclass=ABCMeta):
    DATA_FOLDER = 'downloaded_pdf_files'

    def __init__(self):
        self.processed_download_links: Set = set()
        self.current_row: dict = dict()
        self.session = requests.Session()
        retries = Retry(total=5, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
        self.session.mount("https://", HTTPAdapter(max_retries=retries))

        self.PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent
        self.logger = Logger(self.__class__.__name__)

    @abstractmethod
    def get_download_link(self) -> str:
        pass

    @abstractmethod
    def get_relative_path(self) -> str:
        pass

    @abstractmethod
    def unique_row_generator(self)-> Tuple[str, str, str]:
        pass

    def get_output_filename(self) -> str:
        url = self.get_download_link()
        path = parse.urlparse(url).path
        _, ext = os.path.splitext(path)
        ext = ext.lower()
        if not ext or not ext[1:].isalnum():
            ext = '.bin'

        hashed = hashlib.md5(url.encode("utf-8")).hexdigest()
        return f"{hashed}{ext}"

    def is_valid_row(self)-> bool:
        if not self.current_row:
            return False

        if not self.get_download_link():
            self.logger.warning(f"Download link is not found for {self.current_row}")
            return False

        return True

    def is_processed_row(self, download_link)-> bool:
        if download_link in self.processed_download_links:
            return True

        if self.current_row.get(self.CSV_COL_FULL_PATH):
            if os.path.exists(self.current_row[self.CSV_COL_FULL_PATH]):
                return True

        if self.current_row.get(self.CSV_COL_RELATIVE_PATH):
            if os.path.exists(os.path.join(self.PROJECT_ROOT, self.CSV_COL_RELATIVE_PATH)):
                return True

        return False

    def update_row_processed(self, download_link, filename: str):
        self.processed_download_links.add(download_link)

        if not self.current_row.get(self.CSV_COL_FULL_PATH) or not os.path.exists(self.current_row[self.CSV_COL_FULL_PATH]):
            self.current_row[self.CSV_COL_FULL_PATH] = filename

        relative_path = os.path.relpath(self.current_row[self.CSV_COL_FULL_PATH], self.PROJECT_ROOT)
        if not self.current_row.get(self.CSV_COL_RELATIVE_PATH) or not os.path.exists(os.path.join(self.PROJECT_ROOT, self.CSV_COL_RELATIVE_PATH)):
            self.current_row[self.CSV_COL_RELATIVE_PATH] = relative_path

    def get_final_path(self) -> str:
        relative_path = self.get_relative_path()
        file_name = self.get_output_filename()
        final_path = os.path.join(relative_path, file_name)

        path = pathlib.Path(relative_path)
        path.mkdir(parents=True, exist_ok=True)

        return final_path

    def get_old_relative_path(self) -> str:
        pass

    def get_old_output_filename(self) -> str:
        pass

    def get_old_final_path(self):
        relative_path = self.get_old_relative_path()
        file_name = self.get_old_output_filename()
        final_path = os.path.join(relative_path, file_name)

        path = pathlib.Path(relative_path)
        path.mkdir(parents=True, exist_ok=True)

        return final_path

    def download(self):
        for download_link, file_name, old_format_file_name in self.unique_row_generator():
            if self.is_processed_row(download_link):
                self.logger.info(f"File already exists: {file_name}")
                continue
            else:
                if os.path.exists(old_format_file_name):
                    os.replace(old_format_file_name, file_name)
                    self.logger.info(f"Moved old file: {old_format_file_name} → {file_name}")

                    parent_dir = Path(old_format_file_name).parent
                    while True:
                        if parent_dir.is_dir() and not any(parent_dir.iterdir()):
                            parent_dir.rmdir()
                            self.logger.info(f"Deleted empty folder after move: {parent_dir}")
                            parent_dir = parent_dir.parent
                        else:
                            break
                    continue

            try:
                with (self.session.get(download_link, stream=True, timeout=10) as response):
                    if response.status_code == 200:
                        with open(file_name, 'wb') as file:
                            for chunk in response.iter_content(chunk_size=1024):
                                if chunk:
                                    file.write(chunk)

                        self.logger.info(f"Downloaded: {file_name}")
                    else:
                        self.logger.error(f"Failed to download {download_link}: {response.status_code}")
                        self.logger.error(traceback.format_exc())

            except requests.RequestException as e:
                self.logger.error(f"Failed to download {download_link}: {e}")
                self.logger.error(traceback.format_exc())


class ScraperClassDownloader(BaseDownloader, metaclass=ABCMeta):
    SCRAPER_CLASS: BaseScraper

    def __init__(self):
        super().__init__()
        self.current_processed_file = None
        self.file_name_prefixes: list[str] | None = None

        self.source_data_path: pathlib.Path = self.get_data_path()
        self.destination_data_path: pathlib.Path = self.get_data_path(source=False)

        self.processed_files = set()
        self.current_processed_file_prefix = None
        self.CSV_COL_FULL_PATH = "pdf_downloaded_full_path"
        self.CSV_COL_RELATIVE_PATH = "pdf_downloaded_relative_path"

        self.logger.info(f"Started to process files for {self.__class__.__name__}")


    def get_classes_to_scrape(self):
        try:
            subclasses = self.SCRAPER_CLASS.__subclasses__()
            if not (subclasses and isinstance(subclasses, list)):
                subclasses = [self.SCRAPER_CLASS]
        except Exception as e:
            self.logger.error(f"Failed to get classes to scrape: {e}")
            self.logger.error(traceback.format_exc())
            return []
        else:
            return subclasses

    def get_relative_path(self, extras: list[str] = None) -> str:
        if not extras:
            extras = []

        path = os.path.join(self.destination_data_path, self.current_processed_file_prefix, *extras)

        return path

    def get_file_name_prefixes(self):
        classes_to_scrape = self.get_classes_to_scrape()
        prefixes = []
        for class_ in classes_to_scrape:
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

    def process_file_name_generator(self):
        ### return latest csv file with a prefix. Ex: Konu_Ozetleri_timestamp.csv

        compiled_search = re.compile(r'_(\d{8}_\d{6})\.csv$')
        def extract_timestamp(file_path):
            match = re.search(compiled_search, file_path.name)
            if match:
                return datetime.strptime(match.group(1), '%Y%m%d_%H%M%S')
            return datetime.min

        self.file_name_prefixes = self.get_file_name_prefixes()
        for file_name_prefix in self.file_name_prefixes:
            if not file_name_prefix in self.processed_files:
                files = self.source_data_path.glob(f"{file_name_prefix}_*.csv")
                files = sorted(files, key=extract_timestamp, reverse=True)

                if files:
                    yield file_name_prefix, files[0].absolute()

    def unique_row_generator(self):
        file_names = self.process_file_name_generator()
        for prefix, file_name in file_names:
            try:
                self.current_processed_file_prefix = prefix
                self.processed_files.add(prefix)
                self.logger.info(f"Processing: {prefix}")
                count = 0
                updated_fieldnames = set()
                processed_rows_2_update = list()
                with open(file_name, 'r', encoding='utf-8-sig') as f:
                    reader = csv.DictReader(f)
                    original_fieldnames = list(reader.fieldnames) if reader.fieldnames else []
                    updated_fieldnames = {k: 1 for k in original_fieldnames}
                    updated_fieldnames[self.CSV_COL_FULL_PATH] = 1
                    updated_fieldnames[self.CSV_COL_RELATIVE_PATH] = 1

                    for row in reader:
                        self.current_row = row
                        if self.is_valid_row():
                            link_2_d = self.get_download_link()
                            full_d_path = self.get_final_path()
                            old_full_d_path = self.get_old_final_path()

                            yield link_2_d, full_d_path, old_full_d_path

                            self.update_row_processed(link_2_d, full_d_path)

                            count += 1
                        else:
                            self.current_row[self.CSV_COL_FULL_PATH] = self.current_row[self.CSV_COL_RELATIVE_PATH] = ''

                        processed_rows_2_update.append(self.current_row)

                self.logger.info(f"Total number of processed rows for {prefix}: {count}")

                with open(file_name, 'w', encoding='utf-8-sig', newline="") as f:
                    writer = csv.DictWriter(f, updated_fieldnames.keys())
                    writer.writeheader()
                    writer.writerows(processed_rows_2_update)

                self.logger.info(f"Successfully updated {prefix}: {count}")
            except Exception as e:
                self.logger.error(f"Failed to process {prefix}: {e}")
                self.logger.error(traceback.format_exc())


class ScraperVideoDownloader(ScraperClassDownloader):
    DATA_FOLDER = 'downloaded_video_files'
    YOUTUBE_DOMAINS = ['youtube.com', 'youtu.be']

    def __init__(self):
        super().__init__()
        self.CSV_COL_FULL_PATH = "video_downloaded_full_path"
        self.CSV_COL_RELATIVE_PATH = "video_downloaded_relative_path"

    def is_valid_row(self) -> bool:
        if not super().is_valid_row():
            return False

        link = self.get_download_link()

        parsed = parse.urlparse(link)
        if any([domain in parsed.netloc for domain in self.YOUTUBE_DOMAINS]):
            self.logger.info(f"Skipping youtube video: {link}")
            return False

        return True

    def get_download_link(self) -> str:
        return self.current_row['videoLink']

    def get_old_output_filename(self) -> str:
        unique_id = self.current_row['videoId']
        if '.mp4' not in unique_id:
            unique_id = f"{unique_id}.mp4"

        return unique_id

    def get_old_relative_path(self) -> str:
        return self.get_relative_path()