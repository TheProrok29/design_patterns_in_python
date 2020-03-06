from chair_parts import *


class ChildrenChairsFactory:

    @staticmethod
    def produce_back(*args):
        return Back((10, 15))

    @staticmethod
    def produce_arm(*args):
        return Arm((5, 10), 'red')

    @staticmethod
    def produce_wheel(*args):
        return None

    @staticmethod
    def produce_base():
        return Base('plastic')

    @staticmethod
    def produce_gas_lift(*args):
        return None

    @staticmethod
    def produce_seat(*args):
        return Seat((10, 12), 'red', 'plastic')
