"""
Problem 9: Find the product of the pythagorean triplet for which the sum is 1000.
"""

from . import helpers


def solve():
    # in order for a < b < c, the max value that a can take on is 332, since then, b could be 333 and c could be 334
    max_a = 332

    for i in range(1, max_a + 1):

        # ensures that c >= b
        max_b = (1000 - i) // 2

        for j in range(i + 1, max_b + 1):
            k = 1000 - i - j
            if helpers.is_pythagorean_triplet(i, j, k):
                return i * j * k
