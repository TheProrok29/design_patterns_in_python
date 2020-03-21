from abc import ABC, abstractmethod


class Builder(ABC):

    @abstractmethod
    def _create_back(self):
        pass

    @abstractmethod
    def _create_arms(self):
        pass

    @abstractmethod
    def _create_wheels(self):
        pass

    @abstractmethod
    def _create_base(self):
        pass

    @abstractmethod
    def _create_gas_lift(self):
        pass
