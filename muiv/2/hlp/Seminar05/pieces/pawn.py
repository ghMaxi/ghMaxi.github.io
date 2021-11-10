from .piece import Piece


class Pawn(Piece):
    def symbol(self):
        return 'P'

    def can_reach(self, r1, c1, r2, c2, cells):
        return ''
