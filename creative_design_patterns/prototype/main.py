from creative_design_patterns.prototype.car import Car
from creative_design_patterns.prototype.prototype import Prototype

my_car = Car('Audi', 'TT', 'diesel', 'manual', 'sedan', 'OB7656', 'Tom Bog', color='black', dors=5)
print(my_car)

prototypes = Prototype()
prototypes.add_prototype('1', my_car)

another_car = prototypes.clone('1', license_plate='LU 55 77 33', owner='Ida Bog', color='pink')
print(another_car)
