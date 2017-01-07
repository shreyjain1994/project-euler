"""
Problem 29: How many distinct terms are in the sequence generated by a^b for 2<=a<=100 and 2<=b<=100
"""

sequence = set()

for a in range(2, 101):
    current = a
    for b in range(2, 101):
        current *= a
        sequence.add(current)

print(len(sequence))