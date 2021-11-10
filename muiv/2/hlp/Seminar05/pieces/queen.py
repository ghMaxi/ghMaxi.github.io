from .piece import Piece


class Queen(Piece):
    def symbol(self):
        return 'Q'

    def can_reach(self, r1, c1, r2, c2, cells):

        return ''
