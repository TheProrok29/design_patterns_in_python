from abc import ABC, abstractmethod


class Strategy(ABC):
    def __init__(self):
        self.price = None
        self.velocity = None
        self.max_distance = None
        self.where_am_i = None

    @abstractmethod
    def hit(self, place):
        raise NotImplementedError
