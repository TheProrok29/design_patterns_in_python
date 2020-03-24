from player import *


class PlayerFactory:
    @staticmethod
    def get_player(type_, specific_appearance):
        if type_ == 'Terrorist':
            player = Terrorist(specific_appearance)
        else:
            player = CounterTerrorist(specific_appearance)
        print(f'Player of type {type_} created')
        return player
