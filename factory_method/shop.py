from random import choice

from plastic_bin import PlasticBin

sweets = ['boiledsweet', 'gummy', 'fudge', 'jawbreaker']


class Shop:
    def __init__(self, amount_of_plastic_bins):
        self.plastic_bins = []
        for _ in range(amount_of_plastic_bins):
            type_ = choice(sweets)
            self.plastic_bins.append(PlasticBin(type_))

    def print_shop_info(self):
        for plastic_bin in self.plastic_bins:
            for element in plastic_bin.set_of_sweet:
                print(type(element), end='')
            print()
