from structural.composite.component import Component
from structural.composite.segment import Segment


class Triangle(Component):
    def __init__(self, seg1: Segment, seg2: Segment, seg3: Segment):
        super().__init__()
        self.children = []
        self.add(seg1)
        self.add(seg2)
        self.add(seg3)

    def add(self, component: Segment):
        component.parent = self
        self.children.append(component)

    def remove(self, component: Segment):
        component.parent = None
        self.children.remove(component)

    def is_composite(self):
        return True

    def move(self, a: float, b: float):
        for child in self.children:
            child.move(a, b)
        print('Triangle moved')
