from abc import abstractmethod


class WebPage:
    def __init__(self, fetcher):
        self.fetcher = fetcher

    @abstractmethod
    def show_page(self):
        pass
