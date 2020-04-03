class Back:
    def __init__(self, size):
        self.size = size


class Arm:
    def __init__(self, size, color):
        self.size = size
        self.color = color


class Wheel:
    def __init__(self, color):
        self.color = color


class Base:
    def __init__(self, material):
        self.material = material


class GasLift:
    def __init__(self, material):
        self.material = material


class Seat:
    def __init__(self, size, color, material):
        self.size = size
        self.color = color
        self.material = material
