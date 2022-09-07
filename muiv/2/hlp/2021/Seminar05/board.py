from typing import List, Optional
from pieces.piece import Piece


class Board:
    def __init__(self, width: int, height: int):
        self.cells: List[List[Optional[Piece]]] = list()
        for row in range(width):
            self.cells.append(list())
            for col in range(height):
                self.cells[row].append(None)

    def place(self, piece: Piece, x: int, y: int):
        self.cells[x][y] = piece

    def try_move(self, move_str):
        start_col, start_row, end_col, end_row = move_str
        col_zero = ord('a')
        start_col = ord(start_col) - col_zero
        end_col = ord(end_col) - col_zero
        start_row = 8 - int(start_row)
        end_row = 8 - int(end_row)

        piece = self.cells[start_row][start_col]
        if piece is None:
            return 'нет фигуры'
        move_error = piece.can_move(
                start_row, start_col,
                end_row, end_col, self.cells)
        if move_error:
            return move_error
        else:
            self.cells[start_row][start_col] = None
            self.cells[end_row][end_col] = piece
        return ''
