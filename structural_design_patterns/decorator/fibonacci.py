import time

fib_called = 0


def fib(n):
    global fib_called
    fib_called += 1
    if n < 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    start = time.time()
    print(fib(35))
    stop = time.time()
    print(fib_called)
    print(stop - start)
