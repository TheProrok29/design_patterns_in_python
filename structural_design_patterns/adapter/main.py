from dog import Dog
from child import Child
from dog_costume import DogAdapter

dog1 = Dog(8, 'm', 'shepherd dog', 'brawn')
child1 = Child(8, 'm', 'white')

dog2_child = DogAdapter(child1)
dog1.bark()

dog2_child.say_something('Hello!')
dog2_child.bark()