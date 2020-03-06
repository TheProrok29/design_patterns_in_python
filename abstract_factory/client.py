from random import shuffle

from abstract_factory.manufacturer import ChairX


class Client:
    def __init__(self):
        self.colors = ['red', 'green', 'blue', 'yellow', 'black', 'silver']
        self.materials = ['leather', 'artificial leather', 'plastic']
        self.sizes = [(20, 25), (30, 20), (20, 20), (18, 22)]
        self.types = ['normal', 'exclusive', 'plane', 'children']
        self.chair = None

    def request_chair(self):
        shuffle(self.colors)
        shuffle(self.materials)
        shuffle(self.sizes)
        shuffle(self.types)
        request = {'color': self.colors[0],
                   'material': self.materials[0],
                   'size': self.sizes[0],
                   'type': self.types[0], }
        chosen_manufacture = ChairX(request)
        new_dream_chair = chosen_manufacture.produce_chair()
        self.chair = new_dream_chair
