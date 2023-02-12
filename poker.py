import sys

class Card:
    def __init__(self, ch):
        self.suit = ord(ch) // 16
        self.rank = ord(ch) % 16
        if self.rank > 12:
            self.rank -= 1

def is_straight(hand):
    ranks = sorted([card.rank for card in hand])
    if ranks == [1, 10, 11, 12, 13]:
        return 2
    elif all(x + 1 == y for x, y in zip(ranks, ranks[1:])):
        return 1
    return 0

def counts(xs):
    return sorted([xs.count(x) for x in set(xs)])

def name(hand):
    rc = counts([card.rank for card in hand])
    sc = counts([card.suit for card in hand])
    flush = sc == [5]
    straight = is_straight(hand)

    if straight == 2 and flush: return 'Royal Flush'
    elif straight and flush:    return 'Straight Flush'
    elif 4 in rc:               return 'Four of a Kind'
    elif rc == [2, 3]:          return 'Full House'
    elif flush:                 return 'Flush'
    elif straight:              return 'Straight'
    elif 3 in rc:               return 'Three of a Kind'
    elif rc.count(2) == 2:      return 'Two Pair'
    elif 2 in rc:               return 'Pair'
    else:                       return 'High Card'

for arg in sys.argv[1:]:
    hand = [Card(c) for c in arg]
    print(name(hand))
