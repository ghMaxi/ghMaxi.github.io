class Rank:
    all = list()

    def __init__(self, print_symbol):
        self.print_symbol = print_symbol
        Rank.all.append(self)

    def __str__(self):
        return f"Rank({self.print_symbol})"


two = Rank('2')
three = Rank('3')
four = Rank('4')
five = Rank('5')
six = Rank('6')
seven = Rank('7')
eight = Rank('8')
nine = Rank('9')
ten = Rank('X')
jack = Rank('J')
queen = Rank('Q')
king = Rank('K')
ace = Rank('A')

if __name__ == '__main__':
    print(two, three, four, five)
    print(six, seven, eight, nine)
    print(ten, jack, queen, king, ace)
# результат:
# Rank(2) Rank(3) Rank(4) Rank(5)
# Rank(6) Rank(7) Rank(8) Rank(9)
# Rank(X) Rank(J) Rank(Q) Rank(K) Rank(A)
