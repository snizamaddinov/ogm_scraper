from scrapers.base_scraper import BaseScraper
from bs4 import BeautifulSoup
import re


class KazanimBazliKazanimKavramaEtkinlikScraper(BaseScraper):
    PATH = '/kazanim-kavrama-kazanim-liste'
    FILE_HEADERS = [
        "sinifId", "sinifIsmi", 
        "dersId", "dersNo", "dersKodu", "dersIsmi", 
        "uniteId", "uniteNo", "uniteIsmi",
        "kazanimId", "kazanimNo", "kazanimKod", "kazanimIsmi",
        "pdfId", "pdfBaslik", "pdfLink"
    ]
    PDF_DOWNLOAD_PATH = '/panel/upload/yardimci-kitap/'

    def __init__(self):
        super().__init__()
        self.compiled_patterns['pdf_id'] = re.compile(r"pdfGoster\('([^']+)")

    def scrape(self):
        main_html = self.exponential_backoff_request(f"{self.BASE_URL}{self.PATH}")

        if not main_html:
            return
        
        a_ders_ids, a_unite_ids, a_kazanim_ids = self.parse_ders_unite_kazanim_ids(main_html)
        grade_options = self.fetch_grades(main_html)

        for sinif_id, sinif_ismi in grade_options:
            subjects = self.get_subject_list(sinif_id)

            for subject in subjects:
                if a_ders_ids and subject["id"] not in a_ders_ids:
                    continue

                chapters = self.get_unit_list(subject["id"])
                for chapter in chapters:
                    if a_unite_ids and chapter["id"] not in a_unite_ids:
                        continue
                    
                    file_rows = []
                    gains = self.get_kazanim_list(chapter["id"])
                    for gain in gains:
                        if a_kazanim_ids and gain["id"] not in a_kazanim_ids:
                            continue

                        pdfs = self.get_pdf_items(subject["urlKod"], sinif_id, subject["id"], chapter["id"], gain["id"])
                        for pdf in pdfs:
                            row = [ self.clean_text(item) if isinstance(item, str) else item
                                for item in
                                [sinif_id, sinif_ismi, subject["id"], subject["sira"], subject['kod'], subject["baslik"],
                                chapter["id"], chapter["sira"], chapter["baslik"], gain["id"], gain["sira"],
                                gain["kod"], gain["baslik"], pdf["pdfId"], pdf["pdfBaslik"], pdf["pdfLink"]]
                            ]

                            file_rows.append(row)
                    
                    self.write_to_csv(file_rows)



    def get_pdf_items(self, ders_urlKod, sinif_id: str, ders_id: int, unite_id: int, kazanim_id: int):
        url_page = f"{self.BASE_URL}{self.PATH}/{ders_urlKod}?s={sinif_id}&d={ders_id}&u={unite_id}&k={kazanim_id}"
        soup = self.get_soup_from_url(url_page)

        pdfs = soup.select(".sidebar-content-item a")

        scraped_pdfs = []
        for pdf in pdfs:
            onclick_attr = pdf.get("onclick", "")
            pdf_id_group = self.compiled_patterns['pdf_id'].search(onclick_attr)

            if pdf_id_group:
                pdf_title = pdf.text.strip()
                pdf_id = pdf_id_group.group(1)
                pdf_link = f"{self.BASE_URL}{self.PDF_DOWNLOAD_PATH}{pdf_id}"

                scraped_pdfs.append({
                    "pdfId": pdf_id,
                    "pdfBaslik": pdf_title,
                    "pdfLink": pdf_link
                })

