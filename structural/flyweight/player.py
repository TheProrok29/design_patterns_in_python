from abc import ABC


class Player(ABC):
    def __init__(self, specific_appearance):
        self.weapon = ''
        self.specific_appearance = specific_appearance

    def jump(self):
        print('I jump')

    def assigne_weapon(self, weapon):
        self.weapon = weapon


class Terrorist(Player):
    pass


class CounterTerrorist(Player):
    pass
