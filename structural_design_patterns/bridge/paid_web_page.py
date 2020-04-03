from structural_design_patterns.bridge.web_page import WebPage


class PaidWebPage(WebPage):
    def show_page(self):
        article = self.fetcher.get_article()
        image = self.fetcher.get_image()
        print(image)
        print(article)
