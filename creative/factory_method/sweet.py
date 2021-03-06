from abc import ABC
from random import choice


class Sweet(ABC):
    @classmethod
    def create_sweet(cls, **kwargs):
        raise Exception('You can"t do that.')


class BoiledSweet(Sweet):
    colors = ['red', 'green', 'blue']

    def __init__(self, color):
        if color is not None:
            self.color = color
        else:
            self.color = choice(BoiledSweet.colors)

    @classmethod
    def create_sweet(cls, **kwargs):
        return BoiledSweet(kwargs.get('color', None))


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
    def create_sweet(cls, **kwargs):
        return Gummy(kwargs.get('color', None), kwargs.get('shape', None))


class Jawbreaker(Sweet):
    pass

    @classmethod
    def create_sweet(cls, **kwargs):
        return Jawbreaker()


class Fudge(Sweet):
    ings = ['with poppy sed,', 'without poppy seed']

    def __init__(self, extra_ingredient):
        if extra_ingredient is not None:
            self.extra_ingredient = extra_ingredient
        else:
            self.extra_ingredient = choice(Fudge.ings)

    @classmethod
    def create_sweet(cls, **kwargs):
        return Fudge(kwargs.get('extra_ingredient', None))
