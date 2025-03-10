from scrapers.books_with_no_filtering_base_scraper import BooksWithNoFilteringBaseScraper


__all__ = [
    'YksCikmisSoruKitaplariScraper',
    'MEBIKonuOzetiKitaplariScraper',
    'DortDortlukKonuPekistirmeTestleriScraper',
    'Yks3AdimDenemeSinavlariScraper',
    'Yks3AdmiSoruBankasiScraper',
    'YksKampiScraper',
    'RehberlikScraper'
]

class YksCikmisSoruKitaplariScraper(BooksWithNoFilteringBaseScraper):
    PATH = '/yks-cikmis-soru-kitaplari'
    FILE_NAME_PREFIX = 'YKS_Cikmis_Soru_Kitaplari'

    def __init__(self):
        super().__init__(check_redirect_links=True)


class MEBIKonuOzetiKitaplariScraper(BooksWithNoFilteringBaseScraper):
    PATH = '/mebi-konu-ozetleri'
    FILE_NAME_PREFIX = 'MEBI_Konu_Ozeti_Kitaplari'

    def __init__(self):
        super().__init__(check_redirect_links=True)


class DortDortlukKonuPekistirmeTestleriScraper(BooksWithNoFilteringBaseScraper):
    PATH = '/yks-konu-pekistirme'
    FILE_NAME_PREFIX = 'Dort_Dortluk_Konu_Pekistirme_Testleri'

    def __init__(self):
        super().__init__(check_redirect_links=True)


class Yks3AdimDenemeSinavlariScraper(BooksWithNoFilteringBaseScraper):
    PATH = '/yks-uc-adim-deneme'
    FILE_NAME_PREFIX = 'YKS_3Adim_Deneme_Sinavlari'

    def __init__(self):
        super().__init__(check_redirect_links=True)


class Yks3AdmiSoruBankasiScraper(BooksWithNoFilteringBaseScraper):
    PATH = '/yks-uc-adim'
    FILE_NAME_PREFIX = 'YKS_3Adim_Soru_Bankasi'

    def __init__(self):
        super().__init__(check_redirect_links=False)


class YksKampiScraper(BooksWithNoFilteringBaseScraper):
    PATH = '/yks-kampi'
    FILE_NAME_PREFIX = 'YKS_Kampi'

    def __init__(self):
        super().__init__(check_redirect_links=False)


class RehberlikScraper(BooksWithNoFilteringBaseScraper):
    PATH = '/rehberlik'
    FILE_NAME_PREFIX = 'Rehberlik'

    def __init__(self):
        super().__init__(check_redirect_links=True)


