from functional.state.phone_states import *


class Phone:
    def __init__(self, state=NormalState()):
        self.state = state

    def set_state(self, state):
        self.state = state

    def ring(self):
        self.state.ring()
