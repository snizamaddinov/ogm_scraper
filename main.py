from scrapers.interactive_books_scraper import InteractiveBooksScraper
from scrapers.video_scraper import VideoScraper
from scrapers.guzel_sanatlar_lisesi_kitap_scraper import GuzelSanatlarLisesiKitapScraper
from scrapers.spor_lisesi_kitap_scraper import SporLisesiKitapScraper
from scrapers.kazanim_kavrama_etkinlik_scraper import KazanimKavramaEtkinlikScraper
from scrapers.kazanim_bazli_kazanim_kavrama_etkinlik_scraper import KazanimBazliKazanimKavramaEtkinlikScraper
from scrapers.calisma_defteri_scraper import CalismaDefterScraper

def main():
    # Scrape interactive books
    # books_scraper = InteractiveBooksScraper()
    # books_scraper.scrape()

    # # # Scrape videos
    # video_scraper = VideoScraper()
    # video_scraper.scrape()

    # guzel = GuzelSanatlarLisesiKitapScraper()
    # guzel.scrape()

    # spor = SporLisesiKitapScraper()
    # spor.scrape()

    kazanim = CalismaDefterScraper()
    kazanim.scrape()
if __name__ == "__main__":
    main() 