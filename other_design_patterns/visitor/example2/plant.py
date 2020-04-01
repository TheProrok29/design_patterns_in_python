from abc import ABC


class Plant(ABC):
    def __init__(self, name):
        self.name = name

    def accept_visitor(self, visitor):
        visitor.accept(self)

    def water(self, responsible):
        print(f'{self.name} watered by {responsible}')

    def ear(self, responsible):
        print(f'{self.name} eaten by {responsible}')


class Grass(Plant):
    def __init__(self):
        super().__init__('grass')


class Cherry(Plant):
    def __init__(self):
        super().__init__('cherry')


class Nettle(Plant):
    def __init__(self):
        super().__init__('nettle')
