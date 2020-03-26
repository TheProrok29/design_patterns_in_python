from abc import ABC, abstractmethod


class Strategy(ABC):
    def __init__(self, price_per_kilometer, velocity, max_distance, where_am_i):
        self.price = price_per_kilometer
        self.velocity = velocity
        self.max_distance = max_distance
        self.where_am_i = where_am_i

    @abstractmethod
    def hit(self, place):
        raise NotImplementedError
