from abc import ABC, abstractmethod


class Builder(ABC):

    @abstractmethod
    def set_data(self, data):
        pass

    @abstractmethod
    def save_data(self):
        pass
