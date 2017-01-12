"""
Problem 10: Find sum of all prime numbers less than 2000000.
"""

from . import helpers


def solve():
    total = 0
    gen = helpers.primes()

    while True:
        current = next(gen)
        if current < 2000000:
            total += current
        else:
            break

    return total
