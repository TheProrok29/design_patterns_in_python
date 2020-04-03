from structural.decorator.cache_decorator.cache_decorator import memorize


@memorize
def factorial(n):
    if n < 2:
        return 1
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product
