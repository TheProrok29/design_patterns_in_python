def rec_factorial(n):
    if n < 2:
        return 1
    return n * rec_factorial(n - 1)
