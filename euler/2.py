"""
Problem 2: Find sum of all even terms of the fibonacci sequence that do not exceed 4 million.
"""


def fib():
    """
    Generator of the terms in the fibonnaci sequence; 1,2,3,5,8,13
    """
    first = 1
    second = 1

    while True:
        first, second = second, first + second
        yield first


def solve():
    gen = fib()
    total = 0
    while True:
        current = next(gen)
        if current > 4000000:
            break
        if current % 2 == 0:
            total += current
    return total
