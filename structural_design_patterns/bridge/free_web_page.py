from webpage import WebPage


class FreeWebPage(Webpage):
    def show_page(self):
        snippet = self.fetcher.get_snippet()
        ads = self.fetcher.get_ads()
        full_version = self.fetcher.go_to_full_version()
        print(snippet)
        print(ads)
        print(full_version)
