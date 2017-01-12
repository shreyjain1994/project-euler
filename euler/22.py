"""
Problem 22: What is the total of all the name scores in the file?
"""

from . import helpers


def word_value(word):
    """
    Determine the value of a word where for each letter the values are: a=1, b=2, c=3.....

    >>> word_value("abc")
    6
    >>> word_value("ABC")
    6
    >>> word_value("ZZa")
    53

    :param str word: The word whose value is to be determined.
    :return: int
    """

    word = word.lower().strip()

    # function ord gives the unicode code point of a char, and since ord(a)=97, reduce all values by 96 to make a=1
    return sum(ord(i) - 96 for i in word)


def solve():
    with open(helpers.get_resource_path(22)) as f:
        string = f.read()

    names = [i[1:-1] for i in string.split(",")]
    names.sort()
    total = sum((index + 1) * word_value(name) for index, name in enumerate(names))
    return total
