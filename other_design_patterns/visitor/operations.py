from abc import ABC, abstractmethod


class Operation(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def dog_method(self):
        pass

    @abstractmethod
    def cat_method(self):
        pass

    def execute_method(self):
        method = getattr(self, self.name + '_method')
        method()


class Sound(Operation):
    def dog_method(self):
        print('Woof woof!')

    def cat_method(self):
        print('meow')
