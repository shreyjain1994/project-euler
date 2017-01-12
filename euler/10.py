"""
Problem 10: Find sum of all prime numbers less than 2000000.
"""

from . import helpers


def solve():
    return sum(helpers.primes_sieve(1999999))
