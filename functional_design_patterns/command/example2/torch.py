class Torch:
    def __init__(self, state='off'):
        self.state = state

    def turn_on(self):
        print('Torch turned on')
        self.state = 'on'

    def turn_off(self):
        print('Torch turned off')
        self.state = 'off'
