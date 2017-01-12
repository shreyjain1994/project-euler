"""
Problem 7: What is the 10 001st prime number?
"""

from . import helpers


def solve():
    gen = helpers.primes()
    for i in range(10000):
        next(gen)
    return next(gen)
