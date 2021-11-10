from side import Side
from abc import ABC, abstractmethod


class Piece(ABC):
    def __init__(self, side: Side):
        self.side = side

    def is_enemy(self, other):
        return self.side != other.side

    @abstractmethod
    def symbol(self):
        return 'F'

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        symbol = f'{self.side.symbol}{self.symbol()}'
        return f'{symbol:^4}'

    def can_move(self, r1, c1, r2, c2, cells):
        if r1 == r2 and c1 == c2:
            return "нельзя ходить на месте"
        if cells[r2][c2] and not self.is_enemy(cells[r2][c2]):
            return "нельзя ходить в дружественные фигуры"
        return self.can_reach(r1, c1, r2, c2, cells)

    @abstractmethod
    def can_reach(self, r1, c1, r2, c2, cells):
        return ''
