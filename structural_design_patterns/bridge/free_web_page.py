from structural_design_patterns.bridge.web_page import WebPage


class FreeWebPage(WebPage):
    def show_page(self):
        image = self.fetcher.get_image()
        snippet = self.fetcher.get_snippet()
        ads = self.fetcher.get_ads()
        full_version = self.fetcher.go_to_full_version()
        print(snippet)
        print(image)
        print(ads)
        print(full_version)
