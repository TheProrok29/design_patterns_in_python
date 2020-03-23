import time

fib_called = 0

cache = dict()


def fib(n):
    global fib_called
    fib_called += 1
    if n < 2:
        return 1
    if n in cache:
        return cache[n]
    result = fib(n - 1) + fib(n - 2)
    cache[n] = result
    return result


if __name__ == '__main__':
    start = time.time()
    print(fib(100))
    stop = time.time()
    print(fib_called)
    print(stop - start)
