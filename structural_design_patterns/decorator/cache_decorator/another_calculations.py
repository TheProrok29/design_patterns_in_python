from structural_design_patterns.decorator.cache_decorator.cache_decorator import memorize


@memorize
def calculation(n):
    summary = 0
    if n % 2 == 0:
        for i in range(1, n + 1, 2):
            summary += i
    else:
        for i in range(2, n + 1, 2):
            summary += i
    return 5 * n ** 5 - 4 * n ** 4 - 3 * summary
