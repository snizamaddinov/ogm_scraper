
import requests
import csv
import os
import re
from bs4 import BeautifulSoup
from time import sleep

BASE_URL = "https://ogmmateryal.eba.gov.tr"
HEADERS = {"User-Agent": "Mozilla/5.0"}
FILE_NAME = "interactive_books.csv"
FILE_HEADERS = [
    "sinifId", "sinif", "dersId", "dersNo", "dersIsmi", "uniteId", "uniteNo", "uniteIsmi", "kazanimId", "kazanimNo", "kazanimIsmi",
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

def fetch_json(url, method="GET", data=None):
    sleep(0.3)  # Ensure a delay before each request
    response = requests.request(method, url, headers=HEADERS, json=data)
    if response.status_code == 200:
        return response.json()
    return None

def fetch_html(url):
    sleep(0.3)
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.text
    return None

def get_grades():
    html = fetch_html(f"{BASE_URL}/etkilesimli-kitaplar")
    if not html:
        return []
    soup = BeautifulSoup(html, "html.parser")
    options = soup.select("select#dlSinif option[value]")
    return [(opt["value"], clean_text(opt.text)) for opt in options if opt["value"] != "0"]

def get_subjects(sinifId):
    url = f"{BASE_URL}/api/ders-listele/{sinifId}"
    return fetch_json(url, method="POST") or []

def get_chapters(dersId):
    url = f"{BASE_URL}/api/unite-listele/{dersId}"
    return fetch_json(url, method="POST") or []

def get_gains(uniteId):
    url = f"{BASE_URL}/api/kazanim-listele/{uniteId}"
    return fetch_json(url, method="POST") or []

def get_books(sinifId, dersId, uniteId, kazanimId, urlKod):
    url = f"{BASE_URL}/etkilesimli-kitap/{urlKod}?s={sinifId}&d={dersId}&u={uniteId}&k={kazanimId}"
    html = fetch_html(url)
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
        thumbnailLink = clean_text(img["src"]) if img else ""
        
        interaktifKitapLink = pdfIndirmeLink = zipIndirmeLink = ""
        kitapId = sayfaNo = ""
        
        for a in div.select(".books-detail-action-buttons a"):
            href = clean_text(a.get("href", ""))
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

def scrape():
    grades = get_grades()
    for sinifId, sinif in grades:
        if sinifId == '21':
            continue
        process_grade(sinifId, sinif)

def process_grade(sinifId, sinif):
    subjects = get_subjects(sinifId)
    for subject in subjects:
        if str(sinifId) == '7':
            if str(subject.get('id', '')) != '59':
                continue
        dersId, dersNo, ders, urlKod = subject.get("id"), subject.get("sira"), subject.get("baslik", ""), subject.get("urlKod")
        process_subject(sinifId, sinif, dersId, dersNo, ders, urlKod)

def process_subject(sinifId, sinif, dersId, dersNo, ders, urlKod):
    chapters = get_chapters(dersId)
    for chapter in chapters:
        uniteId, uniteNo, unite = chapter.get("id"), chapter.get("sira"), chapter.get("baslik", "")
        process_chapter(sinifId, sinif, dersId, dersNo, ders, urlKod, uniteId, uniteNo, unite)

def process_chapter(sinifId, sinif, dersId, dersNo, ders, urlKod, uniteId, uniteNo, unite):
    gains = get_gains(uniteId)
    for gain in gains:
        kazanimId, kazanimNo, kazanim = gain.get("id"), gain.get("sira"), gain.get("baslik", "")
        process_gain(sinifId, sinif, dersId, dersNo, ders, urlKod, uniteId, uniteNo, unite, kazanimId, kazanimNo, kazanim)

def process_gain(sinifId, sinif, dersId, dersNo, ders, urlKod, uniteId, uniteNo, unite, kazanimId, kazanimNo, kazanim):
    books = get_books(sinifId, dersId, uniteId, kazanimId, urlKod)
    rows = []
    for book in books:
        row = [clean_text(str(item)) for item in [sinifId, sinif, dersId, dersNo, ders, uniteId, uniteNo, unite, kazanimId, kazanimNo, kazanim,
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
    scrape()
    print("Scraping completed successfully!")