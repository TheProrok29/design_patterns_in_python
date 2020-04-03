from inspect import getmembers, isclass
from random import choice

import sweet

from creative_design_patterns.factory_method.plastic_bin import PlasticBin

sweets = [getattr(sweet, m[0]) for m in getmembers(sweet, isclass)
          if m[1].__module__ == 'sweet' and m[0] != 'Sweet']


class Shop:
    def __init__(self, amount_of_plastic_bins):
        self.plastic_bins = []
        for _ in range(amount_of_plastic_bins):
            type_ = choice(sweets)
            self.plastic_bins.append(PlasticBin(type_))

    def print_shop_info(self):
        for plastic_bin in self.plastic_bins:
            for element in plastic_bin.set_of_sweets:
                print(type(element), end='')
            print()

    def fill(self):
        for plastic_bin in self.plastic_bins:
            for _ in range(plastic_bin.limit):
                plastic_bin.restock()

    def buy(self, how_many, type_):
        for plastic_bin in self.plastic_bins:
            if plastic_bin.sweet_type == type_:
                while how_many and len(plastic_bin.set_of_sweets) > 0:
                    how_many -= 1
                    plastic_bin.get_sweet()
