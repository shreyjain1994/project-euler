"""
Problem 7: What is the 10 001st prime number?
"""

from helpers import primes

gen = primes()
for i in range(10000):
    next(gen)

print(next(gen))
