from abc import ABC, abstractmethod

NOT_IMPLEMENTED = 'You should implement this.'


class AbstractImage(ABC):
    def __init__(self, file_path):
        self.file_path = file_path

    @abstractmethod
    def load_image(self):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def display_image(self):
        raise NotImplementedError(NOT_IMPLEMENTED)


class Image(AbstractImage):
    def load_image(self):
        print('Image loaded.')

    def display_image(self):
        print('Display image.')


class ProxyImage(AbstractImage):
    def __init__(self, image):
        super().__init__(image.file_path)
        self.image_loaded = False
        self.image = image

    def load_image(self):
        self.image.load_image()

    def display_image(self):
        if not self.image_loaded:
            self.load_image()
        self.image.display_image()
