from abc import ABC


class Widget(ABC):
    def __init__(self, parent=None):
        self.parent = parent

    @staticmethod
    def default_handler(event):
        print(f'I don\'t know how to handle {event.name}')

    def handle(self, event):
        handle_name = f'handle_{event.name}'
        if hasattr(self, handle_name):
            handler = getattr(self, handle_name)
            handler(event)
        elif self.parent is not None:
            self.parent.handle(event)
        else:
            self.default_handler(event)
