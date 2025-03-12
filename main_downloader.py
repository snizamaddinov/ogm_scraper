from downloaders.files_with_id_downloader import (
    BooksAndVideoNoFilteringDownloader,
    BooksAndVideoWithFilteringDownloader,
    BooksWithFilteringDownloader,
    BooksWithNoFilteringDownloader,
    BooksWithProgressiveFilteringDownloader,
    PdfLinksWithFilteringDownloader)


def main():
    downloader = PdfLinksWithFilteringDownloader()
    downloader.download()

    BooksWithProgressiveFilteringDownloader().download()
    BooksWithNoFilteringDownloader().download()
    BooksWithFilteringDownloader().download()
    BooksAndVideoWithFilteringDownloader().download()
    BooksAndVideoNoFilteringDownloader().download()



    # d2 =   PdfLinksWithFilteringDownloader()


if __name__ == "__main__":
    main()

