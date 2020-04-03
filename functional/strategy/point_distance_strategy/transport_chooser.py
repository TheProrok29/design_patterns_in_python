import inspect
import sys
from random import choice


class TransportChooser:
    def __init__(self, a, b, strategy=None):
        self.strategy = strategy
        self.a = a
        self.b = b
        self.strategies = inspect.getmembers(
            sys.modules['functional.strategy.point_distance_strategy.strategies'], inspect.isclass)

    def use_strategy(self):
        if self.strategy:
            self.strategy.hit(self.b)
        else:
            choice(self.strategies)[1]().hit(self.b)
