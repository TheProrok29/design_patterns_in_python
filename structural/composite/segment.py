from structural.composite.component import Component
from structural.composite.point import Point


class Segment(Component):
    def __init__(self, p1: Point, p2: Point):
        super().__init__()
        self.children = []
        self.add(p1)
        self.add(p2)

    def add(self, component: Point):
        component.parent = self
        self.children.append(component)

    def remove(self, component: Point):
        component.parent = None
        self.children.remove(component)

    def is_composite(self):
        return True

    def move(self, a: float, b: float):
        for child in self.children:
            child.move(a, b)
        print('Segment moved')
