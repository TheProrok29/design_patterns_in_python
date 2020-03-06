from abstract_factory.chair_parts import *


class PlaneChairsFactory:

    @staticmethod
    def produce_back(*args):
        return Back((20, 40))

    @staticmethod
    def produce_arm(*args):
        return Arm((5, 15), 'blue')

    @staticmethod
    def produce_wheel(*args):
        return None

    @staticmethod
    def produce_base():
        return Base('steel')

    @staticmethod
    def produce_gas_lift(*args):
        return None

    @staticmethod
    def produce_seat(*args):
        return Seat((20, 20), 'blue', 'artificial leather')
