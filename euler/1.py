"""
Problem 1: Find the sum of all the multiples of 3 or 5 below 1000.
"""


def solve():
    multiples_of_three = sum(range(0, 1000, 3))
    multiples_of_five = sum(range(0, 1000, 5))
    multiples_of_fifteen = sum(range(0, 1000, 15))

    # multiples of fifteen are counted as both mul of 3 and 5, hence we need to subtract 1 'set' of them
    return multiples_of_five + multiples_of_three - multiples_of_fifteen
