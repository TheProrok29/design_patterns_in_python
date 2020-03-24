from webpage import WebPage


class Paid WebPage(Webpage):
    def show_page(self):
        article = self.fetcher.article()
        image = self.fetcher.get_image()
        print(image)
        print(article)
