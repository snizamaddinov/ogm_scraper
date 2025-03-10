from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse, parse_qs


def scrape_flibooks(soup: BeautifulSoup, check_redirect_links=False, domain=None)->list[dict[str, str]]:
    books = soup.select('.books-detail-action-content')
    scraped_books = []

    for book in books:
        flipbook_link = ''  
        pdf_link = ''
        zip_link = ''
        thumbnail_link = book.select_one('img')['src']

        for action_link in book.select('.books-detail-action-buttons a'):
            href = action_link['href']

            if check_redirect_links:
                if not href.startswith('http'):
                    href = f"{domain}{href}"
                result_without_redirect = requests.get(href, allow_redirects=False)
                if result_without_redirect.is_redirect:
                    href = result_without_redirect.headers["Location"]

            if href.endswith('.pdf'):
                pdf_link = href
            elif href.endswith('.zip'):
                zip_link = href
            else:
                flipbook_link = href

        
        scraped_books.append({
            'flipbook_link': flipbook_link,
            'pdf_link': pdf_link,
            'zip_link': zip_link,
            'thumbnail_link': thumbnail_link
        })

    return scraped_books


def get_video_data_from_url(url, text_cleaner: callable=None):
    if text_cleaner is None:
        text_cleaner = lambda x: x

    if not url:
        return {
            'id': '',
            'playlist_id': '',
            'time': '',
            'link': ''
        }

    parsed_url = urlparse(url)

    query_params = parse_qs(parsed_url.query)
    playlist_id = query_params.get('list', [None])[0]
    time = query_params.get('t', [None])[0]
    if query_params.get('v'):
        video_id = query_params.get('v')[0]
    else:
        video_id = parsed_url.path.split('/')[-1]

    return {
        'id': video_id,
        'playlist_id': playlist_id,
        'time': text_cleaner(time),
        'link': url
    }