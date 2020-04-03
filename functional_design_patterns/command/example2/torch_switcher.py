from functional_design_patterns.command.example2.command import *


class TorchSwitcher:
    def __init__(self, torch, switch):
        self._torch = torch
        self._switch = switch

    def toggle(self, cmd):
        if cmd.lower() == 'on':
            self._switch.execute(TurnLightOn(self._torch))
        else:
            self._switch.execute(TurnLightOff(self._torch))
