from time_decorator import timer


class Foo:
    def __init__(self, a: int, b: int, text: str):
        self.a = a
        self.b = b
        self.text = text

    @timer
    def do_stuff1(self):
        return sum(x for x in range(self.a, self.b))

    @timer
    def do_stuff2(self):
        for i in range(self.a * self.b):
            self.text = self.text[::-1]

    @timer
    def do_stuff3(self):
        a, b = self.a ** 3, self.b ** 3
        while a != b:
            if a != b:
                if a > b:
                    a -= b
                else:
                    b -= a
