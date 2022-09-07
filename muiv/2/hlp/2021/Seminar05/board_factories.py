from board import Board
from side import Side
from pieces.pawn import Pawn
from pieces.rook import Rook
from pieces.knight import Knight
from pieces.bishop import Bishop
from pieces.queen import Queen
from pieces.king import King


def standard_chess_board():
    board_size = 8
    black = Side('b')
    white = Side('w')
    result = Board(board_size, board_size)
    rear_line = (Rook, Knight, Bishop, Queen,
                 King, Bishop, Knight, Rook)

    for col in range(board_size):
        result.place(rear_line[-1-col](black), 0, col)
        result.place(Pawn(black), 1, col)
        result.place(Pawn(white), 6, col)
        result.place(rear_line[col](white), 7, col)

    return result
