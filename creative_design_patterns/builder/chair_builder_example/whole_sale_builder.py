import time

from creative_design_patterns.builder.chair_builder_example.builder import Builder
from creative_design_patterns.builder.chair_builder_example.chair import Chair
from creative_design_patterns.builder.chair_builder_example.chair_parts import *


class WholeSaleBuilder(Builder):

    def _create_back(self):
        print('I"am creating a back')
        return Back('15x20')

    def _create_arms(self):
        print('I"am creating an arms')
        return [Arm('8x15', 'black') for _ in range(2)]

    def _create_wheels(self):
        print('I"am creating a wheels')
        return [Wheel('black') for _ in range(5)]

    def _create_base(self):
        print('I"am creating a base')
        return Base('metal')

    def _create_gas_lift(self):
        print('I"am creating a gas lift')
        return GasLift('black')

    def _create_seat(self):
        print('I"am creating a seat')
        return Seat('25x25', 'black', 'artificial')

    def create_chair(self):
        print('I"am start creating a chair')
        chair = Chair()
        back = self._create_back()
        chair.back = back

        arms = self._create_arms()
        chair.arms = arms

        wheels = self._create_wheels()
        chair.wheels = wheels

        base = self._create_base()
        chair.base = base

        print('I clamp the wheels in the stand')
        time.sleep(1)

        gas_lift = self._create_gas_lift()
        chair.gas_lift = gas_lift

        print('I attach the jack to the stand')
        time.sleep(1)

        seat = self._create_seat()
        chair.seat = seat

        print('I scratch everything to sit on')
        time.sleep(1)
        print('Chair is ready')

        return chair
