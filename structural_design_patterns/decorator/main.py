import random
import sys
import time

from another_calculations import calculation
from factorial1 import rec_factorial
from factorial2 import factorial
from fibonacci import fib

sys.setrecursionlimit(10 ** 7)

start = time.time()
a = fib(35)
for i in range(10000):
    n = random.randint(1, 2000)
    b, c, d = rec_factorial(n), factorial(n), calculation(n)
stop = time.time()
print(stop - start)
