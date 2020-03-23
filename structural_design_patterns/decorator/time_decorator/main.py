from foo import Foo
from timeit import Timer

obj = Foo(200, 300, 'something')

obj.do_stuff1()
obj.do_stuff2()
obj.do_stuff3()

func = obj.do_stuff1
t = Timer('func()', 'from __main__ import func')
print('Time: ', t.timeit())
