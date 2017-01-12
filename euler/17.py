"""
Problem 17: If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters
would be used?
"""


def num_of_letters(n):
    """
    Determine the number of letters in the word representation of n. Spaces and dashes are not counted.

    >>> num_of_letters(5)
    4
    >>> num_of_letters(64)
    9
    >>> num_of_letters(438)
    25
    >>> num_of_letters(342)
    23
    >>> num_of_letters(115)
    20
    >>> num_of_letters(30)
    6
    >>> num_of_letters(340)
    20
    >>> num_of_letters(300)
    12
    >>> num_of_letters(319)
    23

    :param int n: A number that is between 1 and 1000 inclusive.
    :rtype: int
    """

    words = {0: '',
             1: 'one',
             2: 'two',
             3: 'three',
             4: 'four',
             5: 'five',
             6: 'six',
             7: 'seven',
             8: 'eight',
             9: 'nine',
             10: 'ten',
             11: 'eleven',
             12: 'twelve',
             13: 'thirteen',
             14: 'fourteen',
             15: 'fifteen',
             16: 'sixteen',
             17: 'seventeen',
             18: 'eighteen',
             19: 'nineteen',
             20: 'twenty',
             30: 'thirty',
             40: 'forty',
             50: 'fifty',
             60: 'sixty',
             70: 'seventy',
             80: 'eighty',
             90: 'ninety'}

    if n > 1000 or n < 1:
        raise ValueError("n must be between 1 and 1000 inclusive.")

    if n <= 20:
        return len(words[n])

    elif n < 100:
        tens = int(str(n)[0]) * 10
        ones = int(str(n)[1])
        return len(words[tens]) + len(words[ones])

    elif n < 1000:
        hundreds = int(str(n)[0])
        remainder = n - hundreds * 100
        if remainder > 0:
            return len(words[hundreds]) + len('hundred') + len('and') + num_of_letters(remainder)
        else:
            return len(words[hundreds]) + len('hundred')

    else:
        return 11


def solve():
    total = sum(num_of_letters(i) for i in range(1, 1001))
    return total
