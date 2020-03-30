class Memento:
    def __init__(self):
        self._states = []
        self._i = -1

    def save_state(self, state):
        if self._i != len(self._states) - 1:
            self._states = self._states[:self._i + 1]
        self._states.append(state)
        self._i += 1

    def undo(self):
        if self._i > 0:
            self._i -= 1

    def redo(self):
        if self._i < len(self._states) - 1:
            self._i += 1

    def read_state(self):
        return self._states[self._i]
