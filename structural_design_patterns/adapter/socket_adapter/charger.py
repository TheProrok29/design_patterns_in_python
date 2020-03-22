class Charger:
    def __init__(self, device, socket):
        self.device = device
        self.socket = socket

    def __transformer(self):
        if self.socket.voltage <= self.device.max_voltage:
            return self.socket.voltage
        else:
            voltage = self.socket.voltage
            print('Voltage was changed')
            voltage = self.device.max_voltage
            return voltage

    def plug(self):
        return self.__transformer()
