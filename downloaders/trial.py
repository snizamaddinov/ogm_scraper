import csv

#
# current_row = None
# with open("/Users/bkmobil/Projects/scrapers/ogmmateryal_scraper/data/YKS_Kampi_20250310_134103.csv", encoding='utf-8-sig') as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         current_row = row
#         print(current_row)
#         print(type(current_row))

from requests.adapters import HTTPAdapter

from requests.adapters import HTTPAdapter, Retry
import requests
session = requests.Session()
retries = Retry(total=5, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
session.mount("https://", HTTPAdapter(max_retries=retries))

response = session.get('tarball_url', stream=True, timeout=10)
