class Rank:
    def __init__(self, value, symbol=''):
        self.value = value
        self.symbol =\
            symbol if symbol else str(value)


ten = Rank(10, 'X')
jack = Rank(11, 'J')
queen = Rank(12, 'Q')
king = Rank(13, 'K')
ace = Rank(14, 'A')
two = Rank(2)
three = Rank(3)
four = Rank(4)
five = Rank(5)
six = Rank(6)
seven = Rank(7)
eight = Rank(8)
nine = Rank(9)
all_ranks = (two, three, four, five,
             six, seven, eight, nine,
             ten, jack, queen, king, ace)


class Card:
    def __init__(self, rank: Rank):
        self.rank = rank

    def beats(self, other):
        return self.rank.value > other.rank.value

    def ties(self, other):
        return self.rank.value == other.rank.value

    @property
    def symbol(self):
        return self.rank.symbol


if __name__ == "__main__":
    card1 = Card(ace)
    card2 = Card(two)
    card3 = Card(two)
    print(card1.beats(card2))
    print(card2.ties(card3))
