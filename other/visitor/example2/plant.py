from abc import ABC


class Plant(ABC):
    def __init__(self, name):
        self.name = name

    def accept_visitor(self, visitor):
        visitor.visit(self)

    def water(self, responsible):
        print(f'{self.name} watered by {responsible}')

    def eat(self, responsible):
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
