from abc import ABC, abstractmethod


class Visitor(ABC):
    @abstractmethod
    def visit(self, plant):
        pass


class Human(Visitor):
    def visit(self, plant):
        plant.water(self)


class Cow(Visitor):
    def visit(self, plant):
        plant.eat(self)


class Dog(Visitor):
    def visit(self, plant):
        plant.eat(self)
