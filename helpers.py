"""
Commonly used functions throughout project euler problems.
"""

import math


def is_prime(n):
    """
    Determine if n is a prime number.

    :rtype: bool
    """

    if n < 2:
        return False

    upper_bound = int(math.sqrt(n))

    return not any(n % i == 0 for i in range(2, upper_bound + 1))


def product(ls):
    """
    Determine the product of all the numbers in ls.

    Usage:

    >>> product([1,2,4,5])
    40
    >>> product([-5,8,2])
    -80
    >>> product([3,0,9,87])
    0
    """

    p = 1
    for i in ls:
        p *= i

    return p


def primes():
    """
    An unlimited generator of prime numbers: 2,3,5,7...

    Usage:

    >>> gen = primes()
    >>> next(gen)
    2
    >>> next(gen)
    3
    >>> next(gen)
    5
    """

    yield 2

    i = 1

    while True:
        found_prime = False
        while not found_prime:
            i += 2
            found_prime = is_prime(i)
        yield i
