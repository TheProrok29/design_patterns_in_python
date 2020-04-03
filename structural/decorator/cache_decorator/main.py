import random
import sys
import time

from structural.decorator.cache_decorator.another_calculations import calculation
from structural.decorator.cache_decorator.factorial1 import rec_factorial
from structural.decorator.cache_decorator.factorial2 import factorial
from structural.decorator.cache_decorator.fibonacci import fib

sys.setrecursionlimit(10 ** 7)

start = time.time()
for i in range(10000):
    n = random.randint(1, 2000)
    a, b, c, d = fib(n), rec_factorial(n), factorial(n), calculation(n)
stop = time.time()
print(stop - start)
