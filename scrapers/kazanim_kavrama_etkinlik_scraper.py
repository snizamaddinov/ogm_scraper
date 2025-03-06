from scrapers.base_scraper import BaseScraper
from scrapers.helpers import scrape_flibooks

class KazanimKavramaEtkinlikScraper(BaseScraper):
    PATH = '/kazanim-kavrama-sec'
    BOOK_PATH = '/kazanim-kavrama-etkinlik'
    FILE_HEADERS = [
        "sinifId", "sinifIsmi", "dersId", "dersNo", "dersKodu", "dersIsmi",
        "interaktifKitapLink", "pdfIndirmeLink", "zipIndirmeLink", "kitapThumbnailLink"
    ]

    def scrape(self):
        grades = self.fetch_grades()

        if not grades:
            return

        url = f"{self.BASE_URL}{self.BOOK_PATH}" + "/{subject_urlKod}?s={sinifId}&d={dersId}"

        for sinifId, sinifIsmi in grades:
            subjects = self.get_subject_list(sinifId)

            rows = []
            for subject in subjects:
                formatted_url = url.format(subject_urlKod=subject["urlKod"], sinifId=sinifId, dersId=subject["id"])
                books_html = self.get_soup_from_url(formatted_url)
                
                if not books_html:
                    continue

                books = scrape_flibooks(books_html, check_redirect_links=True, domain=self.BASE_URL)
                for book in books:
                    row = [
                        sinifId, self.clean_text(sinifIsmi), 
                        subject["id"], subject["sira"], subject["kod"], self.clean_text(subject["baslik"]),
                        book["flipbook_link"], book["pdf_link"], book["zip_link"], book["thumbnail_link"]
                    ]

                    rows.append(row)
            
            self.write_to_csv(rows)