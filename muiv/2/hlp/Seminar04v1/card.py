import suit
import rank


class Card:
    def __init__(self, _rank: rank.Rank, _suit: suit.Suit):
        self.suit = _suit
        self.rank = _rank

    def __str__(self):
        return f'Card({self.print_symbol})'

    @property
    def print_symbol(self):
        return f"{self.rank.print_symbol}{self.suit.print_symbol}"


if __name__ == '__main__':
    card = Card(rank.two, suit.hearts)
    print(card)

# результат
# Card(2♥)
