from card import Card, all_ranks
import random


class Deck:
    def __init__(self, *cards):
        self.cards = list(cards)
        random.shuffle(self.cards)

    def __str__(self):
        line = ', '.join(
            card.symbol for card in self.cards)
        return f'Deck({line})'

    def has_cards(self, count=1):
        return len(self.cards) >= count

    def get_top_card(self):
        return self.cards.pop()

    def deal(self, other):
        card = self.cards.pop()
        other.cards.append(card)


deck = Deck(*(Card(rank) for rank
              in all_ranks * 4))


if __name__ == "__main__":
    print(deck)
