from random import choice

from sweet import Sweet


class BoiledSweet(Sweet):
    colors = ['red', 'green', 'blue']

    def __init__(self, color):
        if color is not None:
            self.color = color
        else:
            self.color = choice(BoiledSweet.colors)

    @classmethod
    def create_sweet(cls, color=None):
        return BoiledSweet(color)
