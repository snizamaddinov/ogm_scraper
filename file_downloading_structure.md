## types of files by column characteristic:


## 1. data with file-id field:


###  Only Pdf link with filtering (pdf_links_with_filtering_base_scraper.py)
[
"sinifId", "sinifIsmi",
"dersId", "dersNo", "dersKodu", "dersIsmi",
"uniteId", "uniteNo", "uniteIsmi",
"kazanimId", "kazanimNo", "kazanimKod", "kazanimIsmi",
"pdfId", "pdfBaslik", "pdfLink"
]


### pages with list of books and video links, no filtering (book_and_video_no_filtering_base_scraper.py)
[
"baslik",
"pdfId", "pdfLink",
'videoId', 'playlistId', 'time', 'videoLink'
]



### Special pages with detailed data 
kitapId = pdfId
- Etkileşimli Kitaplar
 - Ders Kitapları

[
"sinifId", "sinifIsmi",
"dersId", "dersNo", "dersKodu", "dersIsmi",
"uniteId", "uniteNo", "uniteIsmi",
"kazanimId", "kazanimNo", "kazanimKod", "kazanimIsmi",
"kitapId", "kitapIsmi", "sayfaNo",
"interaktifKitapLink", "pdfIndirmeLink", "zipIndirmeLink", "kitapThumbnailLink"
]


### pages with list of books and video links, with filtering (book_and_video_with_filtering_base_scraper.py)
[
"dersKodu", "dersIsmi",
"sinavTipi", "konu",
"pdfId", "pdfLink",
'videoId', 'playlistId', 'time', 'videoLink'
]




## 2. data without file-id-like field. need to generate.

### pages with list of books, no filtering (books_with_no_filtering_base_scraper.py)

["flipbookKitapLink", "pdfIndirmeLink", "zipIndirmeLink", "kitapThumbnailLink"]


### pages with list of books, with filtering (books_with_filtering_base_scraper.py)

[
"sinifId", "sinifIsmi",
"dersId", "dersNo", "dersKodu", "dersIsmi",
"interaktifKitapLink", "pdfIndirmeLink", "zipIndirmeLink", "kitapThumbnailLink"
]

### pages with list of books, with progressive filtering - links scraped from the first page (books_with_progressive_filtering_base_scraper.py)

[
"sinifPath", "sinifIsmi", "dersPath", "dersIsmi",
"flipbookKitapLink", "pdfIndirmeLink", "zipIndirmeLink", "kitapThumbnailLink"
]








 - Ders anlatımı (menu)
     - Ders Anlatım Videoları
 [
   "sinifId", "sinifIsmi", "dersId", "dersNo", "dersKod", "dersIsmi", "uniteId", "uniteNo", "uniteIsmi",
   "kazanimId", "kazanimNo", "kazanimKod", "kazanimIsmi", 'videoId', 'videoBaslik', 'videoLink'
   ]