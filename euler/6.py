"""
Problem 6: Find the difference between the sum of the squares of the first one hundred natural numbers and the square
of the sum.
"""


def sum_of_squares(lower, upper):
    """
    Determine the sum of the squares of all the numbers from lower to upper.

    For example: sum_of_squares(1,10) = 1^2 + 2^2 + 3^2 .... + 10^2 = 385

    Usage:

    >>> sum_of_squares(1, 10)
    385

    :param int lower: The lowest number in sequence.
    :param int upper: The highest number in sequence.
    :rtype: int
    """

    return sum(pow(i, 2) for i in range(lower, upper + 1))


def square_of_sum(lower, upper):
    """
    Determine the square of the sum of all the numbers from lower to upper.

    For example: square_of_sum(1,10) = (1+2...+10)^2 = 55^2 = 3025

    Usage:

    >>> square_of_sum(1,10)
    3025

    :param int lower: The lowest number in sequence.
    :param int upper: The highest number in sequence.
    :rtype: int
    """

    # sum of sequence formula
    total = (lower + upper) * (upper - lower + 1) // 2
    return pow(total, 2)


def solve():
    return square_of_sum(1, 100) - sum_of_squares(1, 100)
