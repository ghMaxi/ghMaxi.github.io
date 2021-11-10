from .piece import Piece


class King(Piece):
    def symbol(self):
        return 'K'

    def can_reach(self, r1, c1, r2, c2, cells):
        return ''
