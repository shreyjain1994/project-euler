"""
Problem 39: Find the perimeter <= 1000 for which there is a maximum number of pythagorean triplets.
"""

from . import helpers


def solve():
    max_triplets = 0
    perimeter = None

    for p in range(3, 1001):
        triplets_found = 0
        max_a = p // 3
        for a in range(1, max_a + 1):
            max_b = (p - a) // 2
            for b in range(a, max_b):
                c = p - a - b
                if helpers.is_pythagorean_triplet(a, b, c):
                    triplets_found += 1
        if triplets_found > max_triplets:
            max_triplets = triplets_found
            perimeter = p

    return perimeter
