from random import choice

from sweet import Sweet


class Gummy(Sweet):
    colors = ['red', 'green', 'blue']
    shapes = ['bear', 'baby', 'duck', 'cat', 'dog']

    def __init__(self, color, shape):
        if color is not None:
            self.color = color
        else:
            self.color = choice(Gummy.colors)
        if shape is not None:
            self.shape = shape
        else:
            self.shape = choice(Gummy.shapes)

    @classmethod
    def create_sweet(cls, color=None, shape=None):
        return Gummy(color, shape)
