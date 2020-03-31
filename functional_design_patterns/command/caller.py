class Caller:
    def __init__(self):
        self._commands = []

    def store_command(self, command, data=''):
        self._commands.append((command, data))

    def execute_commands(self):
        for command, data in self._commands:
            command.execute(data)

    def show_commands(self):
        for command, data in self._commands:
            print(command)

    def show_history(self):
        for command, data in self._commands[::-1]:
            print(command)
