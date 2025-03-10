from scrapers.interactive_books_scraper import InteractiveBooksScraper
from scrapers.video_scraper import VideoScraper
from scrapers.yks_hazirlik_menu_no_filtering import *
from scrapers.etkilesimli_kitaplar_menu_progressive_filtering import *
from scrapers.ders_anlatimi_menu_pdf_links_with_filtering import *


def main():
    # Scrape interactive books
    # books_scraper = InteractiveBooksScraper()
    # books_scraper.scrape()

    # # # Scrape videos
    # video_scraper = VideoScraper()
    # video_scraper.scrape()

    # MEBIKonuOzetiKitaplariScraper().scrape()
    # YksCikmisSoruKitaplariScraper().scrape()
    # DortDortlukKonuPekistirmeTestleriScraper().scrape()
    # Yks3AdimDenemeSinavlariScraper().scrape()
    # Yks3AdmiSoruBankasiScraper().scrape()
    # YksKampiScraper().scrape()
    KonuOzetleriScraper().scrape()
    DersAnlatimSunulariScraper().scrape()



    # spor = OyunVeEtkinliklerScraper()
    # spor.scrape()

    # kazanim = DefterimScraper()
    # kazanim.scrape()


if __name__ == "__main__":
    main() 