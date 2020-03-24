from abc import ABC, abstractmethod


class Webpage:
    def __init__(self, fetcher):
        self.fetcher = fetcher

    @abstractmethod
    def show_page(self):
        pass