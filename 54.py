"""
Problem 54: Given a set of poker hands for 2 players, determine the number of hands that player 1 wins.
"""


class Card(object):
    _ranks = {'T': 10,
              'J': 11,
              'Q': 12,
              'K': 13,
              'A': 14}

    _rank_names = {11: 'Jack',
                   12: 'Queen',
                   13: 'King',
                   14: 'Ace'}

    _suits = {'C': 1,
              'D': 2,
              'H': 3,
              'S': 4}

    _suit_names = {1: 'Clubs',
                   2: 'Diamonds',
                   3: 'Hearts',
                   4: 'Spades'}

    def __init__(self, card):
        """
        Create a card object.

        :param str card: A string representing a card. For example, 4S represents a 4 of spades. Use T for 10.
        """
        rank = card[0].upper()
        suit = card[1].upper()
        self.rank = self._ranks[rank] if rank in self._ranks else int(rank)
        self.suit = self._suits[suit]

    def __repr__(self):
        rank = self._rank_names.get(self.rank, str(self.rank))
        suit = self._suit_names[self.suit]
        return "{rank} of {suit}".format(rank=rank, suit=suit)

    def __lt__(self, other):
        return (self.rank, self.suit) < (other.rank, other.suit)


class PokerHand(object):
    def __init__(self, cards):
        """
        Create a poker hand.

        :param list cards: A list containing 5 cards.
        :raises ValueError: if not provided 5 cards in the constructor arguments.
        """

        if len(cards) != 5:
            raise ValueError("There must be 5 cards in a poker hand.")

        self.cards = sorted(cards)

    def _value(self):
        """
        Internal method which provides a value for the poker hand, which can then be used to compare hands.

        :rtype: list
        """

        all_same_suit = all(i.suit == self.cards[-1].suit for i in self.cards)
        consecutive = all(self.cards[i + 1].rank == self.cards[i].rank + 1 for i in range(4))

        # royal flush check, sum of 10,J,Q,K and A is 60
        if all_same_suit and consecutive and sum(i.rank for i in self.cards) == 60:
            return [10, self.cards[-1].suit]

        # straight flush check
        elif all_same_suit and consecutive:
            return [9, self.cards[-1].rank, self.cards[-1].suit]
