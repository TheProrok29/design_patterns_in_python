class Device:
    max_voltage = 12

    def __try_charge(self, input_voltage):
        if input_voltage > self.max_voltage:
            print(
                f'Device burned!. Used to height voltage {input_voltage}!. Max possible voltage is {self.max_voltage}')
        else:
            print('Charging...!')

    def charge(self, input_voltage):
        self.__try_charge(input_voltage)
