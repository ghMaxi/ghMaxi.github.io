from pprint import pprint
from board_factories import standard_chess_board
from board import Board

if __name__ == "__main__":
    board: Board = standard_chess_board()

    pprint(board.cells)

    move_error = ' '
    while move_error:
        move = input("Move (ex: e2e4): ")
        move_error = board.try_move(move)
        if move_error:
            print (move_error)

    pprint(board.cells)

    move_error = ' '
    while move_error:
        move = input("Move (ex: e2e4): ")
        move_error = board.try_move(move)
        if move_error:
            print (move_error)

    pprint(board.cells)
