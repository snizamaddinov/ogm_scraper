import requests
import csv
import os
import re
import time
from bs4 import BeautifulSoup

BASE_URL = "https://ogmmateryal.eba.gov.tr"
HEADERS = {"User-Agent": "Mozilla/5.0"}
FILE_NAME = "interactive_books.csv"
FILE_HEADERS = [
    "sinifId", "sinifIsmi", "dersId", "dersNo", "dersIsmi", "uniteId", "uniteNo", "uniteIsmi", "kazanimId", "kazanimNo", "kazanimKod", "kazanimIsmi",
    "kitapId", "kitapIsmi", "sayfaNo", "interaktifKitapLink", "pdfIndirmeLink", "zipIndirmeLink", "kitapThumbnailLink"
]


def clean_text(text):
    if not text:
        return ""
    apostrophe_variants = [
        '\u2019', '\u2018', '\u2032', '\u0060', '\u00B4', '\u02BC', '\u02BB', '\u02BD', '\u0022',
        '\u201C', '\u201D', '\u201E', '\u2033', '\u2036', '\u275D'
    ]
    pattern = "|".join(apostrophe_variants)
    text = re.sub(pattern, "'", text)
    text = re.sub(r"[\n\r\t]", " ", text)
    text = re.sub(r"\s{2,}", " ", text)
    return text.strip()

def get_kazanim_code(kazanim_ismi):
    match = re.match(r'^[\w.İŞĞÜÇÖıüşğöç]+(?:[\d.İŞĞÜÇÖıüşğöç]*)?\s*-?', kazanim_ismi.strip())
    return match.group(0).strip(" -") if match else ""


def exponential_backoff_request(url, method="GET", data=None, max_retries=5):
    wait_time = 4  # Start with 4 seconds
    for _ in range(max_retries):
        try:
            response = requests.request(method, url, headers=HEADERS, json=data)
            if response.status_code == 200:
                return response.json() if method == "POST" else response.text
        except requests.exceptions.RequestException:
            pass
        print(f"Request failed. Retrying in {wait_time} seconds...")
        time.sleep(wait_time)
        wait_time *= 2  # Exponential backoff
    return None

def get_last_progress():
    if not os.path.exists(FILE_NAME):
        return None
    with open(FILE_NAME, "r", encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        last_row = None
        c = 0
        for row in reader:
            last_row = row  # Read only the last row
            c += 1
       
    if c < 2 or not last_row:
        return None
    return {
        "sinifId": last_row[0], "dersId": last_row[2], "dersNo": int(last_row[3]), "uniteId": last_row[5],
        "uniteNo": int(last_row[6]), "kazanimNo": int(last_row[9])
    }

def remove_partial_entries(progress):
    if not os.path.exists(FILE_NAME):
        return
    temp_file = FILE_NAME + ".tmp"
    with open(FILE_NAME, "r", encoding="utf-8-sig") as f, open(temp_file, "w", encoding="utf-8-sig", newline="") as temp_f:
        reader = csv.reader(f)
        writer = csv.writer(temp_f)
        for row in reader:
            if row[0] == progress["sinifId"] and int(row[9]) >= progress["kazanimNo"]:
                break 
            writer.writerow(row)
    os.replace(temp_file, FILE_NAME)

def fetch_grades():
    html = exponential_backoff_request(f"{BASE_URL}/etkilesimli-kitaplar")
    if not html:
        return []
    soup = BeautifulSoup(html, "html.parser")
    return [(opt["value"], opt.text.strip()) for opt in soup.select("select#dlSinif option[value]") if opt["value"] != "0"]

def get_books(sinifId, dersId, uniteId, kazanimId, urlKod):
    url = f"{BASE_URL}/etkilesimli-kitap/{urlKod}?s={sinifId}&d={dersId}&u={uniteId}&k={kazanimId}"
    html = exponential_backoff_request(url)
    if not html:
        return []
    
    soup = BeautifulSoup(html, "html.parser")
    section = soup.select_one("section.books-detail-action")
    if not section:
        return []
    
    for div in soup.select(".section-title"):
        div.decompose()
    
    kitapIsmiList = [clean_text(h2.text) for h2 in soup.find_all("h2")]
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
            "kitapIsmi": kitapIsmi,
            "kitapId": kitapId,
            "sayfaNo": sayfaNo,
            "interaktifKitapLink": interaktifKitapLink,
            "pdfIndirmeLink": pdfIndirmeLink,
            "zipIndirmeLink": zipIndirmeLink,
            "thumbnailLink": thumbnailLink
        })
    return kitap_data

def process_scraping():
    last_progress = get_last_progress()
    if last_progress:
        remove_partial_entries(last_progress)
    
    grades = fetch_grades()
    for sinifId, sinif in grades:
        if last_progress and sinifId < last_progress["sinifId"]:
            continue
        subjects = exponential_backoff_request(f"{BASE_URL}/api/ders-listele/{sinifId}", method="POST") or []
        for subject in subjects:
            dersId, dersNo, ders, urlKod = int(subject.get("id")), int(subject.get("sira", 0)), subject.get("baslik", ""), subject.get("urlKod")
            if last_progress and sinifId == last_progress["sinifId"] and dersNo < last_progress["dersNo"]:
                continue
            chapters = exponential_backoff_request(f"{BASE_URL}/api/unite-listele/{dersId}", method="POST") or []
            for chapter in chapters:
                uniteId, uniteNo, unite = int(chapter.get("id", 0)), int(chapter.get("sira", 0)), chapter.get("baslik", "")
                if last_progress and sinifId == last_progress["sinifId"] and dersNo == last_progress["dersNo"] and uniteNo < last_progress["uniteNo"]:
                    continue
                gains = exponential_backoff_request(f"{BASE_URL}/api/kazanim-listele/{uniteId}", method="POST") or []
                for gain in gains:
                    kazanimId, kazanimNo, kazanim = int(gain.get("id", 0)), int(gain.get("sira", 0)), gain.get("baslik", "")
                    kazanimKod = get_kazanim_code(kazanim)
                    if last_progress and sinifId == last_progress["sinifId"] and dersNo == last_progress["dersNo"] and uniteNo == last_progress["uniteNo"] and kazanimNo <= last_progress["kazanimNo"]:
                        continue
                    books = get_books(sinifId, dersId, uniteId, kazanimId, urlKod)
                    rows = []
                    for book in books:
                        row = [clean_text(str(item)) for item in [sinifId, sinif, dersId, dersNo, ders, uniteId, uniteNo, unite, kazanimId, kazanimNo, kazanimKod, kazanim,
                            book["kitapId"], book["kitapIsmi"], book["sayfaNo"], book["interaktifKitapLink"],
                            book["pdfIndirmeLink"], book["zipIndirmeLink"], book["thumbnailLink"]]
                            ]
                        rows.append(row)

                    write_to_csv(rows)

def write_to_csv(rows):
    with open(FILE_NAME, "a", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerows(rows)

if __name__ == "__main__":
    if not os.path.exists(FILE_NAME):
        write_to_csv([FILE_HEADERS])
    process_scraping()
    print("Scraping completed successfully!")
