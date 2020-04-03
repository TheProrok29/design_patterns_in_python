from functional.strategy.point_distance_strategy.strategy import Strategy


class Walk(Strategy):
    def __init__(self):
        super().__init__()
        self.price = 0
        self.velocity = 5
        self.max_distance = 20

    def hit(self, place):
        print(f'I went to place {place}')


class Car(Strategy):
    def __init__(self):
        super().__init__()
        self.price = 1
        self.velocity = 60
        self.max_distance = 500

    def hit(self, place):
        print(f'I drove to place {place}')


class Plane(Strategy):
    def __init__(self):
        super().__init__()
        self.price = 5
        self.velocity = 800
        self.max_distance = 10000

    def hit(self, place):
        print(f'I flew to place {place}')
