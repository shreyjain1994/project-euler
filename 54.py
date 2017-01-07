"""
Problem 54: Given a set of poker hands for 2 players, determine the number of hands that player 1 wins.
"""

from collections import Counter
from operator import itemgetter


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

    def value(self):
        """
        Determine a value for the poker hand, which can then be used to compare hands.

        The first value of the returned list represents the value of the ranked hand from Royal Flush=10 to High Card=1.
        If the ranked hand is the same, then the secondary values in the list help differentiate the hands.

        :rtype: list
        """

        all_same_suit = all(i.suit == self.cards[-1].suit for i in self.cards)
        consecutive = all(self.cards[i + 1].rank == self.cards[i].rank + 1 for i in range(4))
        counter = Counter([i.rank for i in self.cards])
        most_common = counter.most_common()

        # need to sort since counter.most_common has arbitrary order for terms that occur same number of times
        most_common.sort(key=itemgetter(1, 0), reverse=True)

        # royal flush check, sum of 10,J,Q,K and A is 60
        if all_same_suit and consecutive and sum(i.rank for i in self.cards) == 60:
            return [10, self.cards[-1].suit]

        # straight flush check
        if all_same_suit and consecutive:
            return [9, self.cards[-1].rank, self.cards[-1].suit]

        # four of a kind check
        if most_common[0][1] == 4:
            return [8] + [i[0] for i in most_common]

        # full house check
        if most_common[0][1] == 3 and most_common[1][1] == 2:
            return [7] + [i[0] for i in most_common]

        # flush check
        if all_same_suit:
            return [6] + [i.rank for i in self.cards[::-1]] + [self.cards[-1].suit]

        # straight check
        if consecutive:
            return [5, self.cards[-1].rank]

        # three of kind check
        if most_common[0][1] == 3:
            return [4] + [i[0] for i in most_common]

        # two pair check
        if most_common[0][1] == 2 and most_common[1][1] == 2:
            return [3] + [i[0] for i in most_common]

        # one pair check
        if most_common[0][1] == 2:
            return [2] + [i[0] for i in most_common]

        return [1] + [i.rank for i in self.cards[::-1]]

    def __lt__(self, other):
        return self.value() < other.value()


player_one_wins = 0

with open("./resources/54.txt") as f:
    for line in f:
        c = [Card(i) for i in line.split(" ")]
        hand_one = PokerHand(c[0:5])
        hand_two = PokerHand(c[5:10])
        if hand_one > hand_two:
            player_one_wins += 1

print(player_one_wins)
