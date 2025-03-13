# Web Scraper for OGM Materyal

This project scrapes all pages from the [OGM Materyal](https://ogmmateryal.eba.gov.tr/) website and saves the data as CSV files inside the `data` folder.
Also it provides scripts to download all the scraped files and videos.

## Installation

1. Clone the repository.
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

Run the scraper to scrape all pages:
```sh
python main.py
```

Run the downloader to download all files and videos:
```sh
python main_downloader.py
```

## Website page and corresponding scraping class structures can be found in the following file:
- `website_page_scrape_structure.md` 

## Downloading files and videos structure is in the following file:
- `file_downloading_structure.md`

## License
No license. 
