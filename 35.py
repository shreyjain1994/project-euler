"""
Problem 35: How many circular primes are there below one million?
"""

import helpers


def rotations(n):
    """
    Determine a list of all rotations of number n. For example, rotations of 197 are: 197, 971, 719.
    Duplicate rotations are not given.

    >>> rotations(197)
    [197, 719, 971]
    >>> rotations(11)
    [11]

    :rtype: list
    """

    r = []
    n = str(n)

    for i in range(len(n)):
        rotation = int(n)

        # need to avoid duplicate rotations. For example, if n=11, only rotation is [11], not [11,11]
        if rotation not in r:
            r.append(rotation)

        n = n[-1] + n[:-1]

    return r


def solve():

    gen = helpers.primes()
    primes = set()

    # generate primes
    while True:
        prime = next(gen)
        if prime < 1000000:
            primes.add(prime)
        else:
            break

    circular_primes = 0

    for prime in primes:
        r = rotations(prime)
        is_circular = all(i in primes for i in r)
        if is_circular:
            circular_primes += 1

    return circular_primes


if __name__ == "__main__":
    print(solve())
