"""
Problem 9: Find the product of the pythagorean triplet for which the sum is 1000.
"""


def is_pythagorean_triplet(a, b, c):
    """
    Determine if a, b, and c are pythagorean triplets. I.e. They make the equation a^2 + b^2 = c^2 true.

    Usage:

    >>> is_pythagorean_triplet(3,4,5)
    True
    >>> is_pythagorean_triplet(3,4,6)
    False

    :rtype: bool
    """

    return pow(a, 2) + pow(b, 2) == pow(c, 2)


# in order for a < b < c, the max value that a can take on is 332, since then, b could be 333 and c could be 334
max_a = 332

for i in range(1, max_a + 1):

    # ensures that c >= b
    max_b = (1000 - i) // 2

    for j in range(i + 1, max_b + 1):
        k = 1000 - i - j
        if is_pythagorean_triplet(i, j, k):
            print(i * j * k)
