from ..chair_parts import *


class ExclusiveChairsFactory:

    @staticmethod
    def produce_back(*args):
        return Back((10, 15))

    @staticmethod
    def produce_arm(*args):
        return Arm((5, 10), 'gold')

    @staticmethod
    def produce_wheel(*args):
        return None

    @staticmethod
    def produce_base():
        return Base('gold')

    @staticmethod
    def produce_gas_lift(*args):
        return None

    @staticmethod
    def produce_seat(*args):
        return Seat((10, 12), 'grey', 'leather')
