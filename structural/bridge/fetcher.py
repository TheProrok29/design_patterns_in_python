from abc import ABC, abstractmethod


class Fetcher(ABC):

    def __init__(self, article):
        self.article = article

    @abstractmethod
    def get_snippet(self):
        pass

    @abstractmethod
    def get_article(self):
        pass

    @abstractmethod
    def get_ads(self):
        pass

    @abstractmethod
    def get_ads(self):
        pass

    @abstractmethod
    def get_image(self):
        pass

    @abstractmethod
    def go_to_full_version(self):
        pass
