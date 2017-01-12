"""
Problem 21: Evaluate the sum of all the amicable numbers under 10000.
"""

from . import helpers


def solve():
    sum_of_divisors = [0] * 10000

    for i in range(1, 10000):
        # need to subtract i since only care about proper divisors of i (i.e. less than i)
        sum_of_divisor = sum(helpers.factors(i)) - i
        sum_of_divisors[i] = sum_of_divisor

    amicable_numbers = set()

    for a in range(1, 10000):
        b = sum_of_divisors[a]
        if b < 10000 and a != b and sum_of_divisors[b] == a:
            amicable_numbers.add(a)
            amicable_numbers.add(b)

    return sum(amicable_numbers)
