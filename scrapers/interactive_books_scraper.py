from scrapers.base_scraper import BaseScraper
from typing import List, Dict
from bs4 import BeautifulSoup

class InteractiveBooksScraper(BaseScraper):
    PATH = 'etkilesimli-kitaplar'
    FILE_HEADERS = [
        "sinifId", "sinifIsmi", "dersId", "dersNo", "dersKodu", "dersIsmi", "uniteId", "uniteNo", "uniteIsmi",
        "kazanimId", "kazanimNo", "kazanimKod", "kazanimIsmi", "kitapId", "kitapIsmi", "sayfaNo",
        "interaktifKitapLink", "pdfIndirmeLink", "zipIndirmeLink", "kitapThumbnailLink"
    ]


    def get_books(self, sinifId: str, dersId: int, uniteId: int, kazanimId: int, urlKod: str) -> List[Dict]:
        url = f"{self.BASE_URL}/etkilesimli-kitap/{urlKod}?s={sinifId}&d={dersId}&u={uniteId}&k={kazanimId}"
        html = self.exponential_backoff_request(url)
        if not html:
            return []
        
        soup = BeautifulSoup(html, "lxml")
        section = soup.select_one("section.books-detail-action")
        if not section:
            return []
        
        for div in soup.select(".section-title"):
            div.decompose()
        
        kitapIsmiList = [self.clean_text(h2.text) for h2 in soup.find_all("h2")]
        kitap_data = []
        
        for i, div in enumerate(section.select(".books-detail-action-content")):
            kitapIsmi = kitapIsmiList[i] if i < len(kitapIsmiList) else ""
            img = div.select_one("img")
            thumbnailLink = img["src"] if img else ""
            
            interaktifKitapLink = pdfIndirmeLink = zipIndirmeLink = ""
            kitapId = sayfaNo = ""
            
            for a in div.select(".books-detail-action-buttons a"):
                href = a.get("href", "")
                if ".aspx" in href or "sayfa" in href:
                    interaktifKitapLink = href
                    kitapId = href.split("Id=")[-1].split("&")[0] if "Id=" in href else ""
                    sayfaNo = href.split("sayfa=")[-1].split("&")[0] if "sayfa=" in href else "0"
                elif ".pdf" in href:
                    pdfIndirmeLink = href
                elif href:
                    zipIndirmeLink = href
            
            kitap_data.append({
                "kitapId": kitapId,
                "kitapIsmi": kitapIsmi,
                "sayfaNo": sayfaNo,
                "interaktifKitapLink": interaktifKitapLink,
                "pdfIndirmeLink": pdfIndirmeLink,
                "zipIndirmeLink": zipIndirmeLink,
                "thumbnailLink": thumbnailLink
            })
        return kitap_data
    
    def scrape(self):
        grades = self.fetch_grades()
        for sinifId, sinifIsmi in grades:
            subjects = self.get_subject_list(sinifId)
            
            for subject in subjects:
                chapters = self.get_unit_list(subject["id"])

                for chapter in chapters:
                    gains = self.get_kazanim_list(chapter["id"])
                    file_rows = []
                    for gain in gains:
                        books = self.get_books(sinifId, subject["id"], chapter["id"], gain["id"], subject["urlKod"])

                        for book in books:
                            row = [self.clean_text(item) if isinstance (item, str) else item
                                for item in
                                [sinifId, sinifIsmi, subject["id"], subject["sira"], subject['kod'], subject["baslik"], chapter["id"],
                                    chapter["sira"], chapter["baslik"], gain["id"], gain["sira"], gain["kod"],
                                    gain["baslik"]] + list(book.values())]
                            
                            file_rows.append(row)

                    self.write_to_csv(file_rows)
                


                    