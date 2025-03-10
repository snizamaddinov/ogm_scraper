import requests
import re
import time
import csv
import os
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def clean_text(text):
    if not text:
        return ""
    apostrophe_variants = [
        '\u2019','\u2018','\u2032','\u0060','\u00B4','\u02BC','\u02BB','\u02BD','\u0022',
        '\u201C','\u201D','\u201E','\u2033','\u2036','\u275D'
    ]
    pattern = "|".join(apostrophe_variants)
    text = re.sub(pattern, "'", text)
    text = re.sub(r"[\n\r\t]", " ", text)
    text = re.sub(r"\s{2,}", " ", text)
    return text.strip()

def exponential_backoff_request(url, method="GET", data=None, max_retries=5):
    wait_time = 4
    for _ in range(max_retries):
        try:
            response = requests.request(method, url, headers=HEADERS, json=data)
            if response.status_code == 200:
                return response.json() if method == "POST" else response.text
        except requests.exceptions.RequestException:
            pass
        time.sleep(wait_time)
        wait_time *= 2
    return None

def get_grade_options():
    html = exponential_backoff_request("https://ogmmateryal.eba.gov.tr/ebatv-ogm/Default.aspx", "GET")
    soup = BeautifulSoup(html, "html.parser")
    options = soup.select("#dlSinif option")
    grade_list = []
    for opt in options:
        sinif_id = opt.get("value", "").strip()
        sinif_name = opt.text.strip()
        if sinif_id and sinif_id != "0":
            grade_list.append((sinif_id, sinif_name))
    return grade_list

def get_ders_list(sinif_id):
    return exponential_backoff_request(f"https://ogmmateryal.eba.gov.tr/api/ders-listele/{sinif_id}", "POST") or []

def get_unite_list(ders_id):
    data = exponential_backoff_request(f"https://ogmmateryal.eba.gov.tr/api/unite-listele/{ders_id}", "POST")
    if not data:
        return [{"id": 0, "baslik": ""}]
    return data

def get_kazanim_list(unite_id):
    data = exponential_backoff_request(f"https://ogmmateryal.eba.gov.tr/api/kazanim-listele/{unite_id}", "POST")
    if not data:
        return [{"id": 0, "baslik": ""}]
    return data

def get_video_items(sinif_id, ders_id, unite_id, kazanim_id):
    url_page = f"https://ogmmateryal.eba.gov.tr/ebatv-ogm/VideoListele.aspx?s={sinif_id}&d={ders_id}&u={unite_id}&k={kazanim_id}"
    html_page = exponential_backoff_request(url_page, "GET")
    if not html_page:
        return []
    soup = BeautifulSoup(html_page, "html.parser")
    items = soup.select("div.sidebar-content-item a")
    return items

def write_to_csv(rows, csv_file):
    file_exists = os.path.isfile(csv_file)
    mode = "a" if file_exists else "w"
    with open(csv_file, mode, encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow([
                "sinifId","sinif","dersId","ders",
                "uniteId","unite","kazanimId","kazanim",
                "videoId","videoBaslik","videoLink"
            ])
        writer.writerows(rows)

def scrape_data():
    csv_file = "video_data.csv"
    for sinif_id, sinif_name in get_grade_options():
        ders_list = get_ders_list(sinif_id)
        for ders in ders_list:
            ders_id = ders.get("id", "0")
            ders_name = ders.get("baslik", "")
            unite_list = get_unite_list(ders_id)
            for unite in unite_list:
                unite_id = unite.get("id", 0)
                unite_name = unite.get("baslik", "")
                kazanim_list = get_kazanim_list(unite_id)
                for kazanim in kazanim_list:
                    kazanim_id = kazanim.get("id", 0)
                    kazanim_name = kazanim.get("baslik", "")
                    items = get_video_items(sinif_id, ders_id, unite_id, kazanim_id)
                    rows_to_write = []
                    for a in items:
                        video_baslik = clean_text(a.get_text())
                        onclick_attr = a.get("onclick", "")
                        match = re.search(r"videoGoster\('([^']+)", onclick_attr)
                        if match:
                            video_id = clean_text(match.group(1))
                            video_link = f"https://ogmmateryal.eba.gov.tr/ebatv-ogm/upload/uzev-480/{video_id}"
                            rows_to_write.append([
                                sinif_id,
                                clean_text(sinif_name),
                                ders_id,
                                clean_text(ders_name),
                                unite_id,
                                clean_text(unite_name),
                                kazanim_id,
                                clean_text(kazanim_name),
                                video_id,
                                video_baslik,
                                video_link
                            ])
                    if rows_to_write:
                        write_to_csv(rows_to_write, csv_file)

scrape_data()
x