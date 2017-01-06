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
