"""
Problem 36: Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
"""

from euler import helpers


def solve():
    # bin(i) returns text with 0b in front of the actual binary number, hence the slice from 2 onwards
    return sum(i for i in range(1, 1000000) if helpers.is_palindrome(i) and helpers.is_palindrome(bin(i)[2:]))


if __name__ == "__main__":
    print(solve())
