import math


def is_prime(n):
    """
    Determine if n is a prime number.

    :rtype: bool
    """

    if n < 2:
        return False

    upper_bound = int(math.sqrt(n))

    return not any(n % i == 0 for i in range(2, upper_bound + 1))


def largest_prime_factor(n):
    """
    Determine the largest factor of n that is a prime number.

    :rtype: int
    """

    upper_bound = int(math.sqrt(n))

    # the largest factor found so far
    highest = None

    for i in range(2, upper_bound + 1):
        if n % i == 0:
            factor1 = i
            factor2 = n // i

            if is_prime(factor2):
                highest = factor2
                break
            elif is_prime(factor1):
                highest = factor1

    return highest


print(largest_prime_factor(600851475143))