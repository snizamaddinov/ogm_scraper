from downloaders.pdf_downloaders import (
    BooksAndVideoNoFilteringDownloader,
    BooksAndVideoWithFilteringDownloader,
    BooksWithFilteringDownloader,
    BooksWithNoFilteringDownloader,
    BooksWithProgressiveFilteringDownloader,
    PdfLinksWithFilteringDownloader)

from downloaders.video_downloaders import (
BooksAndVideoWithFilteringVideoDownloader,
BooksAndVideoNoFilteringVideoDownloader,
VideoDownloader
)


def pdf_downloader():
    BooksAndVideoNoFilteringDownloader().download()
    BooksAndVideoWithFilteringDownloader().download()
    BooksWithFilteringDownloader().download()
    BooksWithNoFilteringDownloader().download()
    BooksWithProgressiveFilteringDownloader().download()
    PdfLinksWithFilteringDownloader().download()

def video_downloader():
    BooksAndVideoWithFilteringVideoDownloader().download()
    BooksAndVideoNoFilteringVideoDownloader().download()
    VideoDownloader().download()


if __name__ == "__main__":
    pdf_i = input("Do you want to download pdfs? (y/n): ")
    video_i = input("Do you want to download videos? (y/n): ")

    if pdf_i.lower() == 'y':
        pdf_downloader()
    else:
        print("No pdfs will be downloaded.")

    if video_i.lower() == 'y':
        video_downloader()
    else:
        print("No videos will be downloaded.")
