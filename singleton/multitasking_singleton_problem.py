from multiprocessing import Process

from singleton.singleton import Singleton


# Singleton problem with multitasking/multiprocessing/threading
def f(return_list):
    instance = Singleton()
    print(id(instance))
    return_list.append(instance)
    return instance


if __name__ == '__main__':
    return_list = []
    p1 = Process(target=f, args=(return_list,))
    p2 = Process(target=f, args=(return_list,))
    p3 = Process(target=f, args=(return_list,))
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    print(return_list)
# We have a 3 different objects when we create Singleton in the same time and empty list.
