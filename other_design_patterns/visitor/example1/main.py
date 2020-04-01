from animals import Dog
from operations import Sound


def accept_visitor(visitor):
    visitor.execute_method()


my_dog = Dog()
my_dog.accept_visitor = accept_visitor
dog_sound = Sound('dog')

my_dog.accept_visitor(dog_sound)
