"""
Problem 50: Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""

from . import helpers


def solve():
    # create list of primes
    gen = helpers.primes()
    primes = []
    while True:
        current = next(gen)
        if current >= 1000000:
            break
        else:
            primes.append(current)

    primes_set = set(primes)

    longest_chain = 0
    longest_chain_prime = None

    total = 0
    for index, value in enumerate(primes):
        if sum(primes[index:index - longest_chain:-1]) > 1000000:
            break
        total += value
        length = index + 1
        if total in primes_set:
            longest_chain = length
            longest_chain_prime = total
        else:
            total2 = total
            length2 = length
            for i in range(0, index - longest_chain):
                total2 -= primes[i]
                length2 -= 1
                if total2 in primes_set:
                    longest_chain = length2
                    longest_chain_prime = total2

    return longest_chain_prime
