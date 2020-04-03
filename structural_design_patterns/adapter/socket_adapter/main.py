from structural_design_patterns.adapter.socket_adapter.charger import Charger
from structural_design_patterns.adapter.socket_adapter.device import Device
from structural_design_patterns.adapter.socket_adapter.sockets import EuropeanSocket

device = Device()
socket = EuropeanSocket()
charger = Charger(device, socket)
device.charge(charger.plug())
