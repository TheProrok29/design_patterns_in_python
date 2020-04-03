from functional.strategy.sum_strategy.sums import *


def sum_list(int_list: List[int]):
    if len(int_list) < 100:
        return sum_list1(int_list)
    elif len(int_list) < 10 ** 5:
        return sum_list3(int_list)
    else:
        return sum_list2(int_list)
