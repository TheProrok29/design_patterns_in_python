from caller import Caller
from command import Command
from receiver import Receiver

tool = Receiver()
cmd1 = Command(tool)
cmd2 = Command(tool)
caller = Caller()

caller.store_command(cmd1, 'do sth1')
caller.store_command(cmd2, 'do sth2')
# caller.execute_commands()
caller.show_history()
