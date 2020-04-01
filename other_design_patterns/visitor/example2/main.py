from random import choice

from plant import *
from visitor import *

plants = [Grass, Nettle, Cherry]
my_plants = []

for _ in range(10):
    plant = choice(plants)
    my_plants.append(plant())

visitors = [Human, Cow, Dog]
my_visitors = []

for _ in range(10):
    visitor = choice(visitors)
    my_visitors.append(visitor())

for _ in range(10):
    plant = choice(my_plants)
    visitor = choice(my_visitors)
    plant.accept_visitor(visitor)
