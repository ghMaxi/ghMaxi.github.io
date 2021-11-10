from .piece import Piece


class Bishop(Piece):
    def symbol(self):
        return 'B'

    def can_reach(self, r1, c1, r2, c2, cells):
        return ''
