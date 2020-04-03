from functional.command.example2.switch import Switch
from functional.command.example2.torch import Torch
from functional.command.example2.torch_switcher import TorchSwitcher

my_torch = Torch()
my_switcher = Switch()
my_torch_switcher = TorchSwitcher(my_torch, my_switcher)
command = 'on'
my_torch_switcher.toggle(command)
my_torch_switcher.toggle(command)
my_torch_switcher.toggle(command)
command = 'off'
my_torch_switcher.toggle(command)

print(my_switcher.get_history())
