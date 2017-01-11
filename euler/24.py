"""
Problem 24: What is the millionth lexicographic permutation of the digits 0,1,2,3,4,5,6,7,8,9.
"""

from itertools import permutations

gen = permutations("0123456789")
for i in range(1000000 - 1):
    next(gen)

print("".join(next(gen)))
