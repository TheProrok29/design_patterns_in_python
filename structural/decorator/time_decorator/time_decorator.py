import time


def timer(func):
    def wrapper(*args):
        start = time.time()
        func(*args)
        stop = time.time()
        print(stop - start)

    return wrapper
