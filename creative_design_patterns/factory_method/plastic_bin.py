from creative_design_patterns.factory_method.sweet import Sweet

colors = ['red', 'green', 'blue']
shapes = ['bear', 'baby', 'duck', 'cat', 'dog']
ings = ['with poppy sed,', 'without poppy seed']


class PlasticBin:
    def __init__(self, sweet_type: Sweet):
        self.sweet_type = sweet_type
        self.limit = 100
        self.minimum = 10
        self.set_of_sweets = {self.sweet_type.create_sweet(color='red') for _ in range(10)}

    def restock(self):
        if len(self.set_of_sweets) >= self.limit:
            return
        self.set_of_sweets.add(self.sweet_type.create_sweet())

    def get_sweet(self):
        return self.set_of_sweets.pop()
