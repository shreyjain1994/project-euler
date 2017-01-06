"""
Problem 10: Find sum of all prime numbers less than 2000000.
"""

from helpers import primes

total = 0
gen = primes()

while True:
    current = next(gen)
    if current < 2000000:
        total += current
    else:
        break

print(total)
