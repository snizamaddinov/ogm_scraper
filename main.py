from scrapers.interactive_books_scraper import InteractiveBooksScraper
from scrapers.video_scraper import VideoScraper
from scrapers.guzel_sanatlar_lisesi_kitap_scraper import GuzelSanatlarLisesiKitapScraper
from scrapers.spor_lisesi_kitap_scraper import SporLisesiKitapScraper
from scrapers.kazanim_kavrama_etkinlik_scraper import KazanimKavramaEtkinlikScraper
from scrapers.kazanim_bazli_kazanim_kavrama_etkinlik_scraper import KazanimBazliKazanimKavramaEtkinlikScraper
from scrapers.calisma_defteri_scraper import CalismaDefterScraper
from scrapers.kavram_ogretimi_etkilesimli_kitap_scraper import KavramOgrenimiEtkilesimliKitapScraper
from scrapers.kazanim_bazli_kavram_ogretimi_etkilesimli_kitap_scraper import KazanimBazliKavramOgrenimiEtkilesimliKitapScraper
from scrapers.oyun_ve_etkinlikler_scraper import OyunVeEtkinliklerScraper
from scrapers.liseye_hos_geldin import LiseyeHosGeldinScraper
from scrapers.defterim_scraper import DefterimScraper
from scrapers.beceri_temelli_etkilesimli_kitaplar import BeceriTemelliEtkilesimliKitaplarScraper
from scrapers.yks_hazirlik_menu_no_filtering import *




def main():
    # Scrape interactive books
    # books_scraper = InteractiveBooksScraper()
    # books_scraper.scrape()

    # # # Scrape videos
    # video_scraper = VideoScraper()
    # video_scraper.scrape()

    MEBIKonuOzetiKitaplariScraper().scrape()
    YksCikmisSoruKitaplariScraper().scrape()
    DortDortlukKonuPekistirmeTestleriScraper().scrape()
    Yks3AdimDenemeSinavlariScraper().scrape()
    Yks3AdmiSoruBankasiScraper().scrape()
    YksKampiScraper().scrape()
    RehberlikScraper().scrape()
    



    # spor = OyunVeEtkinliklerScraper()
    # spor.scrape()

    # kazanim = DefterimScraper()
    # kazanim.scrape()


if __name__ == "__main__":
    main() 