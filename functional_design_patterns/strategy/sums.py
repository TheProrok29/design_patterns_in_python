import functools
from typing import List


def sum_list1(int_list: List[int]) -> int:
    result_sum = 0
    for num in int_list:
        result_sum += num
    return result_sum


def sum_list2(int_list: List[int]) -> int:
    return sum(int_list)


def sum_list3(int_list: List[int]) -> int:
    return functools.reduce(lambda x, y: x + y, int_list)
