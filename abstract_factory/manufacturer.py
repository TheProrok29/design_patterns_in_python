from chair import Chair
from children_chair_factory import ChildrenChairsFactory
from exclusive_chair_factory import ExclusiveChairsFactory
from office_chair_factory import OfficeChairsFactory
from plane_chair_factory import PlaneChairsFactory


class ChairX:
    def __init__(self, client_options: dict):
        self.client_options = client_options
        self.chair_fab = OfficeChairsFactory()
        self.chair_apple = ExclusiveChairsFactory()
        self.chair_plane = PlaneChairsFactory()
        self.chair_child = ChildrenChairsFactory()

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
        if self.client_options['type'] == 'normal':
            factory = self.chair_fab
        elif self.client_options['type'] == 'exclusive':
            factory = self.chair_apple
        elif self.client_options['type'] == 'plane':
            factory = self.chair_plane
        elif self.client_options['type'] == 'children':
            factory = self.chair_child
        else:
            factory = self.chair_fab
        back, arms, wheels, base, gas_lift, seat = self._request_parts(factory)
        return Chair(back, arms, wheels, base, gas_lift, seat)
