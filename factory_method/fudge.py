from random import choice

from sweet import Sweet


class Fudge(Sweet):
    ings = ['with poppy sed,', 'without poppy seed']

    def __init__(self, extra_ingredient):
        if extra_ingredient is not None:
            self.extra_ingredient = extra_ingredient
        else:
            self.extra_ingredient = choice(Fudge.ings)

    @classmethod
    def create_sweet(cls, extra_ingredient=None):
        return Fudge(extra_ingredient)
