from structural.bridge.fetcher import Fetcher


class SportFetcher(Fetcher):
    def get_snippet(self):
        return self.article[:100]

    def get_article(self):
        return self.article

    def get_ads(self):
        return 'Some sports ads'

    def get_image(self):
        return 'Sport image'

    def go_to_full_version(self):
        return 'Buy full version now!'
