from memento import Memento

my_memento = Memento()

my_memento.save_state('1')
my_memento.save_state('2')
my_memento.save_state('3')
my_memento.save_state('4')
my_memento.save_state('5')

my_memento.undo()
my_memento.undo()
print(my_memento.read_state())

my_memento.save_state('6')

print(my_memento.read_state())

my_memento.redo()

print(my_memento.read_state())
my_memento.undo()
print(my_memento.read_state())
