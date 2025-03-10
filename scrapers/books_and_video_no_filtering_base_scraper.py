from scrapers.base_scraper import BaseScraper
from urllib.parse import urlparse, parse_qs

class BookAndVideoNoFilteringBaseScraper(BaseScraper):
    PATH = ''
    FILE_HEADERS = [ 
        "baslik",
        "pdfId", "pdfLink",
        'videoId', 'playlistId', 'time', 'videoLink'
    ]
    
    def scrape(self):
        html = self.get_soup_from_url(f"{self.BASE_URL}{self.PATH}")
        if not html:
            return
        
        rows = []
        items = html.select('.ogm-yks-item')
        
        for item in items:
            title = item.select_one('.yks-item-head').text or ''
            title = self.clean_text(title)
            contents = item.select('.yks-item-content-buttons')

            for content in contents:
                pdf_link = content.select_one('.button-pdf a').get('href')
                pdf_id = pdf_link.split('/')[-1]

                video_link = content.select_one('.button-youtube a').get('href')
                video = self.get_video_data_from_url(video_link)

                row = [
                    title,
                    pdf_id, pdf_link,
                    video['id'], video['playlist_id'], video['time'], video['link']
                ]

                rows.append(row)
        
        self.write_to_csv(rows)
    
    def get_video_data_from_url(self, url):
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
            'time': self.clean_text(time),
            'link': url
        }
        
        