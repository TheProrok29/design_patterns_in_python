class DogAdapter:
    def __init__(self, child):
        self.child = child

    def bark(self):
        print('Hau Hau')

    def say_something(self, sth):
        self.child.say_something(sth)
