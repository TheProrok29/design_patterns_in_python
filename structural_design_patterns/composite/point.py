from structural_design_patterns.composite.component import Component


class Point(Component):
    def __init__(self, x: float, y: float):
        super().__init__()
        self.x = x
        self.y = y

    def move(self, a: float, b: float):
        self.x += a
        self.y += b
        print('Point moved')
