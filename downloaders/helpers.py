import requests
import time
import re
from urllib import parse


def request_with_backoff(url: str, backoff: int = 2, retries: int = 3) -> requests.Response | None:
    print("Making request to : ", url)
    # return None
    for i in range(retries):
        response = requests.get(url)
        if response.status_code == 200:
            return response
        time.sleep(backoff * i)

    return None

def format_folder_name(text: str)->str:
    turkish_characters_to_english = {
        "ç": "c",
        "ğ": "g",
        "ı": "i",
        "ö": "o",
        "ş": "s",
        "ü": "u",
    }
    text = text.lower()

    text = text.translate(str.maketrans(turkish_characters_to_english))

    text = re.sub(r'[^a-z0-9\s]', ' ', text)

    text = re.sub(r'\s+', '_', text).strip('_')

    return text

def format_filename_from_url(url: str, static_part=None):
    if static_part:
        url = url.replace(static_part, "")

    parsed = parse.urlparse(url)
    return format_folder_name(parsed.path)


