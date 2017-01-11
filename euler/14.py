"""
Problem 14: Which starting number, under one million, produces the longest Collatz sequence?
"""


class Collatz:
    def __init__(self):

        # for key k, this dict holds the length of the collatz sequence starting from k
        self._lengths = {1: 1, 2: 2}

    def length(self, n):
        """
        Determine the length of the collatz sequence starting from n.

        :param int n: The starting term of the collatz sequence.
        :rtype: int
        """

        if n in self._lengths:
            return self._lengths[n]

        chain_length = 0
        current = n

        while current != 1:
            chain_length += 1

            if current % 2 == 0:
                current //= 2
            else:
                current = 3 * current + 1

            if current in self._lengths:
                chain_length += self._lengths[current]
                break

        self._lengths[n] = chain_length
        return chain_length


collatz = Collatz()

# the starting value with the longest collatz chain
max_length_term = 1

# the length of the longest collatz chain
max_length = 1

for i in range(1, 1000000):
    length = collatz.length(i)
    if length > max_length:
        max_length = length
        max_length_term = i

print(max_length_term)
