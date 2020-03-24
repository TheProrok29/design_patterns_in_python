from abc import ABC


class Player(ABC):
    def __init__(self, weapon, specific_appearance):
        self.weapon = weapon
        self.specific_appearance = specific_appearance

    def jump(self):
        print('I jump')


class Terrorist(Player):
    pass


class CounterTerrorist(Player):
    pass
