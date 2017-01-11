"""
What is the sum of the digits of the number 2^1000?
"""

number = pow(2, 1000)
total = sum([int(i) for i in str(number)])
print(total)
