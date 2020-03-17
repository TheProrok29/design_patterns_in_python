from random import randint

from boiled_sweet import BoiledSweet
from fudge import Fudge
from gummy import Gummy
from jawbreaker import Jawbreaker

colors = ['red', 'green', 'blue']
shapes = ['bear', 'baby', 'duck', 'cat', 'dog']
ings = ['with poppy sed,', 'without poppy seed']


class PlasticBin:
    def __init__(self, type_: str):
        self.type = type_
        self.limit = 100
        self.minimum = 10
        if self.type == 'boiledsweet':
            self.set_of_sweet = {BoiledSweet(colors[i % 3]) for i in range(10)}
        elif self.type == 'gummy':
            self.set_of_sweet = {Gummy(colors[i % len(colors)], shapes[i % len(shapes)]) for i in range(10)}
        elif self.type == 'fudge':
            self.set_of_sweet = {Fudge(ings[i % len(ings)]) for i in range(10)}
        else:
            self.set_of_sweet = {Jawbreaker() for _ in range(10)}

    def restock(self):
        if len(self.set_of_sweet) < self.minimum:
            if self.type == 'boiledsweet':
                self.set_of_sweet.add(BoiledSweet(colors[randint(0, len(colors))]))
            elif self.type == 'gummy':
                self.set_of_sweet.add(Gummy(colors[randint(0, len(colors))], shapes[randint(0, len(shapes))]))
            elif self.type == 'fudge':
                self.set_of_sweet.add(Fudge(ings[randint(0, len(ings))]))
            else:
                self.set_of_sweet.add(Jawbreaker())

    def get_sweet(self):
        return self.set_of_sweet.pop()


if __name__ == '__main__':

    plastic_bin_1 = PlasticBin('gummy')
    plastic_bin_2 = PlasticBin('fudge')
    for _ in range(5):
        plastic_bin_1.get_sweet()
        plastic_bin_2.get_sweet()

    plastic_bin_1.restock()
    plastic_bin_2.restock()

    print(plastic_bin_1.set_of_sweet)
    print(plastic_bin_2.set_of_sweet)
