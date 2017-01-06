"""
Problem 5: What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

# answer must be multiple of 380 to be divisible by 20 and 19
i = 380

# optimize the values to check - the missing values are factors of 20 or 19, so no need to check them
to_check = [3, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18]

while True:
    if all(i % j == 0 for j in to_check):
        print(i)
        break
    else:
        i += 380
