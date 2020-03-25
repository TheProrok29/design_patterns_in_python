from abc import ABC, abstractmethod


class AbstractImage(ABC):
    def __init__(self, file_path):
        self.file_path = file_path

    @abstractmethod
    def load_image(self):
        pass

    @abstractmethod
    def display_image(self):
        pass
