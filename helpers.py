"""
Commonly used functions throughout project euler problems.
"""

import math


def is_prime(n):
    """
    Determine if n is a prime number.

    :rtype: bool
    """

    if n <= 1:
        return False
    elif n <= 3:
        return True

    # is even number -> uses bit operation, small optimization but may be worth it if calling this function often
    elif n & 1 == 0:
        return False

    upper_bound = int(math.sqrt(n))

    # odd numbers can only have odd factors, so increment is 2
    return not any(n % i == 0 for i in range(3, upper_bound + 1, 2))


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
    >>> [next(gen) for i in range(20)]
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
    """

    yield 2

    i = 1

    while True:
        i += 2
        while not is_prime(i):
            i += 2
        yield i


def factors(n, sort=False):
    """
    Create a list of all factors of n.

    Usage:

    >>> factors(4, sort=True)
    [1, 2, 4]
    >>> factors(28, sort=True)
    [1, 2, 4, 7, 14, 28]
    >>> factors(9, sort=True)
    [1, 3, 9]
    >>> factors(105, sort=True)
    [1, 3, 5, 7, 15, 21, 35, 105]

    :param bool sort: Whether or not to sort the factors list. Defaults to False
    :param int n: The numbers to find the factors of.
    :rtype: list
    """

    f = []

    upper_bound = int(math.sqrt(n))

    # since odd numbers only have odd factors, this will ensure only odd numbers are checked as factors when n is odd
    # this will cut the number of mod operations required by half when given an odd number
    increment = n % 2 + 1

    for i in range(1, upper_bound + 1, increment):
        if n % i == 0:
            f.append(i)
            f.append(n // i)

    # needed to remove duplicate factor when n is a perfect square.
    # i.e. n=4 would create the list [1,4,2,2] and thus need to remove duplicate 2
    # could potentially use sets to avoid duplicates, but too much overheard in comparison to this
    if f[-2] == f[-1]:
        f.pop()

    if sort:
        f.sort()

    return f
