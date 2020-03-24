from abc import abstractmethod


class WebPage:
    def __init__(self, fetcher):
        self.fetcher = fetcher

    @abstractmethod
    def show_page(self):
        pass

    def __str__(self):
        return f'Interface: {self.__class__}, Implementation: {self.fetcher.__class__}'
