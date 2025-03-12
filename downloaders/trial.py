import csv

current_row = None
with open("/Users/bkmobil/Projects/scrapers/ogmmateryal_scraper/data/YKS_Kampi_20250310_134103.csv", encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    for row in reader:
        current_row = row
        print(current_row)
        print(type(current_row))