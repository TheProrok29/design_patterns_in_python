from random import choice
from player_factory import PlayerFactory


class CounterGame:
    types = ['Terrorist', 'Counter Terrorist']
    weapons = ['AK-47', 'M4A1', 'SG552', 'AUG A1', 'Colt']
    appearance = {'Terrorist': 'Ter1 Ter2 Ter3 Ter4'.split(),
                  'Counter Terrorist': 'CTer1 CTer2 CTer3 CTer4'.split()}

    def __init__(self):
        self.players = []

    def main_game(self):
        for _ in range(20):
            type_ = self.get_random_type()
            appearance = self.get_random_appearance(type_)
            player = PlayerFactory.get_player(type_, appearance)
            player.assigne_weapon(self.get_random_weapon())
            self.players.append(player)

    def get_random_weapon(self):
        return choice(self.weapons)

    def get_random_type(self):
        return choice(self.types)

    def get_random_appearance(self, type_):
        return choice(self.appearance[type_])
