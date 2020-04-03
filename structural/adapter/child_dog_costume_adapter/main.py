from structural.adapter.child_dog_costume_adapter.child import Child
from structural.adapter.child_dog_costume_adapter.dog import Dog
from structural.adapter.child_dog_costume_adapter.dog_costume import DogAdapter

dog1 = Dog(8, 'm', 'shepherd dog', 'brawn')
child1 = Child(8, 'm', 'white')

dog2_child = DogAdapter(child1)
dog1.bark()

dog2_child.say_something('Hello!')
dog2_child.bark()
