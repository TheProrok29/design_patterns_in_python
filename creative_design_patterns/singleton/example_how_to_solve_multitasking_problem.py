# One way to resolve this problem is using shared object
from multiprocessing import Process, Manager

from creative_design_patterns.singleton.singleton import Singleton


def f(return_list):
    instance = Singleton()
    return_list.append(instance)
    return instance


if __name__ == '__main__':
    return_list = Manager().list()
    p1 = Process(target=f, args=(return_list,))
    p2 = Process(target=f, args=(return_list,))
    p3 = Process(target=f, args=(return_list,))
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    for element in return_list:
        print(id(element))
    print(return_list)
# We're still creating 3 different object but we return and add to list the same one object.

# Best way is not use Singleton with threads and multiprocessing when we not must.
