"""
Problem 20: Find the sum of the digits in the number 100!
"""

import math

number = math.factorial(100)
total = sum(int(i) for i in str(number))
print(total)
