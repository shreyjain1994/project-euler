"""
Problem 3: What is the largest prime factor of the number 600851475143?
"""

import math
from . import helpers


def largest_prime_factor(n):
    """
    Determine the largest factor of n that is a prime number.

    :rtype: int
    """

    upper_bound = int(math.sqrt(n))

    # the largest factor found so far
    highest = None

    for i in range(2, upper_bound + 1):
        if n % i == 0:
            factor1 = i
            factor2 = n // i

            if helpers.is_prime(factor2):
                highest = factor2
                break
            elif helpers.is_prime(factor1):
                highest = factor1

    return highest


def solve():
    return largest_prime_factor(600851475143)
