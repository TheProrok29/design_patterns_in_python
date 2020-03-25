from abc import ABC, abstractmethod

NOT_IMPLEMENTED = 'You should implement this.'


class Component(ABC):
    def __init__(self):
        self._parent = None

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent):
        self._parent = parent

    def add(self, component):
        raise NotImplementedError(NOT_IMPLEMENTED)

    def remove(self, component):
        raise NotImplementedError(NOT_IMPLEMENTED)

    def is_composite(self):
        return False

    @abstractmethod
    def move(self, a: float, b: float):
        pass
