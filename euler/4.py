"""
Problem 4: Find the largest palindrome made from the product of two 3-digit numbers.
"""

from euler import helpers


def largest_palindrome(n):
    """
    Determine the largest palindrome made from a product of two n-digit numbers.

    :rtype: int
    """

    # the smallest n-digit number
    lower = pow(10, n - 1)

    # the largest n-digit number
    upper = pow(10, n) - 1

    largest = 0

    for i in range(lower, upper + 1):
        for j in range(i, upper + 1):
            product = i * j
            if product > largest and helpers.is_palindrome(product):
                largest = product

    return largest


print(largest_palindrome(3))
