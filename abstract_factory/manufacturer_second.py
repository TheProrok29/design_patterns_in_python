from chair import Chair

from abstract_factory import UniversalFactory


class ChairY:
    def __init__(self, client_options: dict):
        self.client_options = client_options

    def _request_parts(self, factory):
        wheels = [factory.produce_wheel(self.client_options['color']) for _ in range(5)]
        wheels = None if wheels[0] is None else wheels
        back = factory.produce_back(self.client_options['size'])
        arm1 = factory.produce_arm(self.client_options['size'], self.client_options['color'])
        arm2 = factory.produce_arm(self.client_options['size'], self.client_options['color'])
        base = factory.produce_base()
        gas_lift = factory.produce_gas_lift(self.client_options['color'])
        seat = factory.produce_seat(self.client_options['size'], self.client_options['color'],
                                    self.client_options['material'])
        return back, [arm1, arm2], wheels, base, gas_lift, seat

    def produce_chair(self):
        factory = UniversalFactory.get_factory(self.client_options['type'])
        back, arms, wheels, base, gas_lift, seat = self._request_parts(factory)
        return Chair(back, arms, wheels, base, gas_lift, seat)
