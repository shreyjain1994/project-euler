"""
Problem 30: Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

# the powers of 5 are stored so no need to repeatedly compute powers
powers = {i: i ** 5 for i in range(10)}

# at this point the number is growing much too fast for the sum to catch up
# could possibly optimize this upper_bound even more
upper_bound = 300000

total = sum([i for i in range(upper_bound) if sum(powers[j] for j in [int(k) for k in str(i)]) == i])

# remove the number 1 since despite 1 = 1^5, 1^5 isn't a sum.
total -= 1

print(total)
