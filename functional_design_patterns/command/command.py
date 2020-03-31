class Command:
    def __init__(self, receiver):
        self._receiver = receiver

    def execute(self, data=''):
        print('Command delegate to receiver.')
        self._receiver.execute(data)
