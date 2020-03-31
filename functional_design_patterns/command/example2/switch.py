from collections import deque


class Switch:
    def __init__(self):
        self.history = deque()

    def execute(self, command):
        self.history.appendleft(command)
        command.execute()

    def get_history(self):
        return self.history
