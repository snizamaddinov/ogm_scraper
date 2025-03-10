from scrapers.books_and_video_no_filtering_base_scraper import BookAndVideoNoFilteringBaseScraper

__all__ = ['YKSKampiPdfVideoScraper', 'CevrimiciDenemelerScraper']


class YKSKampiPdfVideoScraper(BookAndVideoNoFilteringBaseScraper):
    PATH = '/yks-kampi'
    FILE_NAME_PREFIX = 'Yks_Kampi_Pdf_Video'


class CevrimiciDenemelerScraper(BookAndVideoNoFilteringBaseScraper):
    PATH = '/yks-deneme-sinavlari'
    FILE_NAME_PREFIX = 'Cevrimici_Denemeler'

    def scrape(self):
        html = self.get_soup_from_url(f"{self.BASE_URL}{self.PATH}")
        if not html:
            print('Failed to fetch html')
            return
        
        rows = []
        table_rows = html.select('table tr')
        for row in table_rows:
            cells = row.select('td')
            if not cells:
                continue

            title = cells[0].text
            pdf_link = cells[1].select_one('a').get('href')
            pdf_id = pdf_link.split('/')[-1]

            video_link = cells[2].select_one('a').get('href')
            video = self.get_video_data_from_url(video_link)

            row = [
                title,
                pdf_id, pdf_link,
                video['id'], video['playlist_id'], video['time'], video['link']
            ]

            rows.append(row)
        
        self.write_to_csv(rows)