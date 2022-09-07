from .piece import Piece


class Rook(Piece):
    def symbol(self):
        return 'R'

    def can_reach(self, r1, c1, r2, c2, cells):
        dir_r = r2 - r1
        dir_c = c2 - c1
        if dir_r != 0 != dir_c:
            return "Ладья не ходит по диагонали"
        dir_r = 1 if dir_r > 0 else -1 if dir_r < 0 else 0
        dir_c = 1 if dir_c > 0 else -1 if dir_c < 0 else 0

        r1 += dir_r
        c1 += dir_c
        while r1 != r2 or c1 != c2:
            if cells[r1][c1]:
                return "Ладья не ходит сквозь фигуры"
            r1 += dir_r
            c1 += dir_c
        return ''
