from ..chair_parts import *


class OfficeChairsFactory:

    @staticmethod
    def produce_back(size):
        return Back(size)

    @staticmethod
    def produce_arm(size, color):
        return Arm(size, color)

    @staticmethod
    def produce_wheel(color):
        return Wheel(color)

    @staticmethod
    def produce_base():
        return Base('plastic')

    @staticmethod
    def produce_gas_lift(color):
        return Base(color)

    @staticmethod
    def produce_seat(size, color, material):
        return Seat(size, color, material)
