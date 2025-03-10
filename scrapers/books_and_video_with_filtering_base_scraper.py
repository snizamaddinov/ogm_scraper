from scrapers.base_scraper import BaseScraper
import re
from scrapers.helpers import get_video_data_from_url

class BooksAndVideoWithFilteringBaseScraper(BaseScraper):
    PATH = ''
    FILE_HEADERS = [
        "dersKodu", "dersIsmi",
        "sinavTipi", "konu",
        "pdfId", "pdfLink",
        'videoId', 'playlistId', 'time', 'videoLink'
    ]

    def __init__(self):
        super().__init__()

        self.compiled_patterns['video_link'] = re.compile(r"videoGoster\('([^']+)")

    def scrape(self):
        subjects = self.fetch_subjects()
        for subject_kod, subject_name in subjects:
            url = f"{self.BASE_URL}{self.PATH}?kod={subject_kod}"

            soup = self.get_soup_from_url(url)
            if not soup:
                continue

            rows = []
            items = soup.select('.sidebar-content-item')
            for item in items:
                sinav_tipi = item.select_one('.head-category').get_text() or ''
                sinav_tipi = self.clean_text(sinav_tipi)

                konu = item.select_one('.head-text').get_text() or ''
                konu = self.clean_text(konu)

                action_links = item.select('.content-item-action a')
                pdf_id = pdf_link = video_id = playlist_id = time = video_link = ''

                for link in action_links:
                    href = link.get('href', '')
                    if '.pdf' in href:
                        pdf_id = href.split('/')[-1]
                        pdf_link = href
                    else:
                        onclick_attr = link.get('onclick')
                        if onclick_attr:
                            video_url = self.compiled_patterns['video_link'].search(onclick_attr)
                            if video_url:
                                video_url = video_url.group(1)
                                video = get_video_data_from_url(video_url)
                                video_id = video['id']
                                playlist_id = video['playlist_id']
                                time = video['time']
                                video_link = video['link']
                
                # row = [
                #     self.clean_text( subject_kod), self.clean_text(subject_name),
                #     self.clean_text(sinav_tipi), self.clean_text(konu),
                #     self.clean_text(pdf_id), pdf_link,
                #     video_id, playlist_id, self.clean_text(time), video_link
                # ]
                row = [
                    self.clean_text(item)
                    for item in [
                        subject_kod, subject_name,
                        sinav_tipi, konu,
                        pdf_id, pdf_link,
                        video_id, playlist_id, time, video_link
                    ]
                ]
                rows.append(row)

            self.write_to_csv(rows)







        