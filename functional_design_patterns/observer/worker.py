from random import randint

from observable import Observable


class Worker(Observable):
    def __init__(self):
        super().__init__()
        self.progress = 0
        self.limit = 100

    def do_work(self, *args, **kwargs):
        self.progress += randint(1, 10)
        self.progress = self.limit if self.progress > self.limit else self.progress
        self.notify(self, *args, **kwargs)
