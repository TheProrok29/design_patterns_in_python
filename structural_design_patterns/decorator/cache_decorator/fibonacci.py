from structural_design_patterns.decorator.cache_decorator.cache_decorator import memorize


@memorize
def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    print(fib(100))
