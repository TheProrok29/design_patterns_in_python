from structural.bridge.fetcher import Fetcher


class WarFetcher(Fetcher):
    def get_snippet(self):
        return self.article[:80]

    def get_article(self):
        return self.article

    def get_ads(self):
        return 'Some weapon ads'

    def get_image(self):
        return 'War image'

    def go_to_full_version(self):
        return 'Full version - now for only 5$ '
