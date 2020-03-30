from abc import ABC


class Widget(ABC):
    def __init__(self, parent=None):
        self.parent = parent

    @staticmethod
    def default_handler(event):
        print(f'I don\'t know how to handle {event}')
