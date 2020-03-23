from foo import Foo
import time

obj = Foo(2000, 3000, 'something')
functions = [obj.do_stuff1, obj.do_stuff2, obj.do_stuff3]
for function in functions:
    start = time.time()
    function()
    stop = time.time()
    print(stop - start)
