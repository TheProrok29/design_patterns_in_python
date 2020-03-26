from time import time

from strategy import sum_list
from sums import *

lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista2 = [x ** 2 for x in range(1, 1000)]
lista3 = [2 * x + 1 for x in range(1, 1000000)]

# start = time()
# sum_list1(lista3)
# stop = time()
# print(stop - start)
#
# start = time()
# sum_list2(lista3)
# stop = time()
# print(stop - start)
#
# start = time()
# sum_list3(lista3)
# stop = time()
# print(stop - start)

start = time()
sum_list(lista3)
stop = time()
print(stop - start)
