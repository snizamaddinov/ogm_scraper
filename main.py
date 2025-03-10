from scrapers.interactive_books_scraper import InteractiveBooksScraper
from scrapers.video_scraper import VideoScraper

from scrapers.etkilesimli_kitaplar_menu_no_filtering import *
from scrapers.etkilesimli_kitaplar_menu_with_filtering import *
from scrapers.etkilesimli_kitaplar_menu_progressive_filtering import *
from scrapers.etkilesimli_kitaplar_menu_pdf_links_with_filtering import *

from scrapers.ders_anlatimi_menu_pdf_links_with_filtering import *

from scrapers.yks_hazirlik_menu_no_filtering import *
from scrapers.yks_hazirlik_menu_book_and_video_no_filtering import *
from scrapers.yks_hazirlik_menu_book_and_video_with_filtering import *

def main():
    # ders kitaplari
    InteractiveBooksScraper().scrape()

    # konu anlatim videolari
    VideoScraper().scrape()

    # yks hazirlik menu
    YksCikmisSoruKitaplariScraper().scrape()
    MEBIKonuOzetiKitaplariScraper().scrape()
    DortDortlukKonuPekistirmeTestleriScraper().scrape()
    Yks3AdimDenemeSinavlariScraper().scrape()
    Yks3AdmiSoruBankasiScraper().scrape()
    YksKampiScraper().scrape()
    RehberlikScraper().scrape()

    YKSKampiPdfVideoScraper().scrape()
    CevrimiciDenemelerScraper().scrape()

    YksKonuAnlatimlariVideoScraper().scrape()

    # etkilesimli kitaplar menu
    SporLisesiKitapScraper().scrape()
    LiseyeHosGeldinScraper().scrape()

    KavramOgrenimiEtkilesimliKitapScraper().scrape()
    KazanimKavramaEtkinlikScraper().scrape()
    CalismaDefterScraper().scrape()
    BeceriTemelliEtkilesimliKitaplarScraper().scrape()

    GuzelSanatlarLisesiKitapScraper().scrape()
    OyunVeEtkinliklerScraper().scrape()
    DefterimScraper().scrape()

    KazanimBazliKazanimKavramaEtkinlikScraper().scrape()
    KazanimBazliKavramOgrenimiEtkilesimliKitapScraper().scrape()
    KazanimBazliBeceriTemelliEtkinlikKitapScraper().scrape()

    KonuOzetleriScraper().scrape()
    DersAnlatimSunulariScraper().scrape()
    





if __name__ == "__main__":
    main() 