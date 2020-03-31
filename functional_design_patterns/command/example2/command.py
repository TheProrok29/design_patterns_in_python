from abc import ABC, abstractmethod


class Command(ABC):
    def __init__(self, torch):
        self.torch = torch

    @abstractmethod
    def execute(self):
        pass


class TurnLightOn(Command):
    def execute(self):
        self.torch.turn_on()


class TurnLightOff(Command):
    def execute(self):
        self.torch.turn_off()
