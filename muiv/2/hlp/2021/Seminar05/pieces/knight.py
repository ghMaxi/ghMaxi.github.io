from .piece import Piece


class Knight(Piece):
    def symbol(self):
        return 'K'

    def can_reach(self, r1, c1, r2, c2, cells):
        dir_r = r2 - r1
        dir_c = c2 - c1
        if (dir_r != 0 and dir_c != 0 and
           abs(dir_r) + abs(dir_c) == 3):
            return ''
        else:
            return 'конь ходит буквой Г'
