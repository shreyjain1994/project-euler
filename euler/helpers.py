"""
Commonly used functions throughout project euler problems.
"""

import math
import os


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


def primes_sieve(highest):
    """
    Generates all primes up to and including the max number using the sieve algorithm as
    explained at https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes with some other little optimizations of my own.

    >>> gen = primes_sieve(71)
    >>> list(gen)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
    >>> gen = primes_sieve(70)
    >>> list(gen)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67]

    :param highest: The upper bound of the prime numbers that are found.
    """

    if highest < 2:
        return
    yield 2
    if highest == 2:
        return

    sieve = [1] * (highest + 1)

    # by starting at 3, it saves us the step of negating all even values in the sieve
    current = 3

    while True:
        yield current

        # remove multiples of current primes
        # choosing to increment by 2*current each time since if I increment by just current, we get an even number(since
        # two odd numbers added give even number) and there is no point in negating an even number in the sieve. By
        # incrementing by 2*current each time, we are guaranteed only the odd multiples of current, and thus we save
        # about half the negating steps.
        i = current + current*2
        while i <= highest:
            sieve[i] = 0
            i += current*2

        # find next prime
        # choosing to increment by 2 since the prime numbers can only be odd and we started with 3 (having yielded 2)
        i = current + 2
        while i <= highest:
            if sieve[i]:
                current = i
                break
            i += 2

        # no more primes
        if i > highest:
            break


def is_palindrome(n, case_sensitive=False):
    """
    Determine if n is a palindrome (i.e. reads the same backwards and forwards). If n is not a string, then the string
    representation of n will be checked instead.

    >>> is_palindrome(505)
    True
    >>> is_palindrome(2918)
    False
    >>> is_palindrome("hello")
    False
    >>> is_palindrome("racecar")
    True
    >>> is_palindrome("RacEcar", case_sensitive=True)
    False
    >>> is_palindrome("RaCecar")
    True

    :param n: The text to check to see if it is a palindrome.
    :param bool case_sensitive: Whether to incorporate capitalization in check for palindrome.
    :rtype: bool
    """

    text = str(n).lower() if not case_sensitive else str(n)
    return text == text[::-1]


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


def get_resource_path(number):
    """
    Get the path of the resource for a particular euler problem.

    :param number: The euler problem for which the resource is required.
    :rtype: str
    """
    resource = "../resources/{}.txt".format(number)
    return os.path.join(os.path.dirname(__file__), resource)


def is_pythagorean_triplet(a, b, c):
    """
    Determine if a, b, and c are pythagorean triplets. I.e. They make the equation a^2 + b^2 = c^2 true.

    Usage:

    >>> is_pythagorean_triplet(3,4,5)
    True
    >>> is_pythagorean_triplet(3,4,6)
    False

    :rtype: bool
    """

    return a * a + b * b == c * c
