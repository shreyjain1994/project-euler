"""
Problem 25: What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""


def fib():
    """
    Generator of the terms in the fibonacci sequence; 1,1,2,3,5,8,13

    >>> gen = fib()
    >>> next(gen)
    1
    >>> next(gen)
    1
    >>> next(gen)
    2
    >>> next(gen)
    3
    >>> next(gen)
    5
    """
    first = 0
    second = 1

    while True:
        first, second = second, first + second
        yield first


def solve():
    gen = fib()
    index = 0
    while True:
        index += 1
        if len(str(next(gen))) == 1000:
            break

    return index
