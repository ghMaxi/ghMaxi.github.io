import random
from card import Card
from suit import Suit, hearts, clubs
from rank import Rank, two, three


class Stack:
    @classmethod
    def shuffled(cls, *cards: Card):
        new_stack = cls(*cards)
        new_stack.shuffle()
        return new_stack

    def __init__(self, *cards: Card):
        self.cards = list(cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def __str__(self):
        line = ', '.join(card.print_symbol
                         for card in self.cards)
        return f'Stack({line})'

    def has_cards(self, card_count):
        return len(self.cards) >= card_count

    def deal_card(self, other):
        card = self.cards.pop()
        other.cards.append(card)

def standard_deck_52():
    card_list = []
    for suit in Suit.all:
        for rank in Rank.all:
            card = Card(suit, rank)
            card_list.append(card)
    return Stack.shuffled(*card_list)


if __name__ == '__main__':
    print(standard_deck_52())
# результат:
# Stack(♥2, ♣3)
