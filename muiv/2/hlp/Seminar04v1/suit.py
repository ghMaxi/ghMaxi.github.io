class Suit:
    all = list()

    def __init__(self, print_symbol):
        self.print_symbol = print_symbol
        Suit.all.append(self)

    def __str__(self):
        return f"Suit({self.print_symbol})"


hearts = Suit('♥')
diamonds = Suit('♦')
clubs = Suit('♣')
spades = Suit('♠')


if __name__ == '__main__':
    print(hearts, diamonds, clubs, spades)

# результат:
# Suit(♥) Suit(♦) Suit(♣) Suit(♠)
