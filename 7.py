"""
Problem 7: What is the 10 001st prime number?
"""

from helpers import primes

gen = primes()
current = None
for i in range(10001):
    current = next(gen)

print(current)
