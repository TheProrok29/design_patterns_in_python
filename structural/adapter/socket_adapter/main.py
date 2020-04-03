from structural.adapter.socket_adapter.charger import Charger
from structural.adapter.socket_adapter.device import Device
from structural.adapter.socket_adapter.sockets import EuropeanSocket

device = Device()
socket = EuropeanSocket()
charger = Charger(device, socket)
device.charge(charger.plug())
