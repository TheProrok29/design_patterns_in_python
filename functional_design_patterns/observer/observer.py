from abc import ABC, abstractmethod

from functional_design_patterns.observer.observable import Observable


class Observer(ABC):
    def __init__(self, observable: Observable):
        observable.add_observer(self)

    @abstractmethod
    def notify(self, *args, **kwargs):
        raise NotImplementedError
