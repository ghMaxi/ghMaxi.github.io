# 3) модули
# каждый модуль - отдельный файл
# модули можно импортировать

print("Начало работы")

import lec01 as chess_boards
board = chess_boards.ChessBoard()
board.place_figure(1, 1, "Вася")
from pprint import pprint
pprint(board.cells)
