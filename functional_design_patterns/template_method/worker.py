from abc import ABC, abstractmethod


class Worker(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def prepare_for_work(self):
        pass

    @abstractmethod
    def go_to_work(self):
        pass

    def log_in(self):
        print(f'Logged in as {self.name}')

    @abstractmethod
    def start_up(self):
        pass

    @staticmethod
    def make_tea():
        print('Tea made')

    @abstractmethod
    def do_work(self):
        pass

    def have_dinner(self):
        print(f'ate something as {self.name} ')

    def work_day(self):
        self.prepare_for_work()
        self.go_to_work()
        self.log_in()
        self.start_up()
        self.make_tea()
        self.do_work()
        self.have_dinner()
