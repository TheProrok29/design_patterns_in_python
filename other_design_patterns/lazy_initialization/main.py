from other_design_patterns.lazy_initialization.car import Car

car1 = Car('PTY77', 'gasoline')
car2 = Car('AZF47', 'electro')
car3 = Car('Vobium', 'diesel')

visitor1 = 'Tom'
visitor2 = 'John'
visitor3 = 'Elen'
visitor4 = 'Mirka'

print('visitor1')
car1.take_a_look(visitor1)
car1.request_additional_informations()
car1.test_drive(visitor1)

print('visitor2')
car1.take_a_look(visitor2)
car2.take_a_look(visitor2)
car3.take_a_look(visitor2)

print('visitor3')
car2.take_a_look(visitor3)
car1.take_a_look(visitor3)
car3.take_a_look(visitor3)
car2.test_drive(visitor3)
car1.test_drive(visitor3)

print('visitor4')
car3.take_a_look(visitor4)
car3.request_additional_informations()
