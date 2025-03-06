from bs4 import BeautifulSoup
import requests

def scrape_flibooks(soup: BeautifulSoup, check_redirect_links=True)->list[dict[str, str]]:
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