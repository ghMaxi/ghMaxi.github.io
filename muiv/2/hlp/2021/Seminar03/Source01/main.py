import random
import tkinter
from typing import List


turn_count: int = 0
bomb_matrix: List[List[int]] = list()
BOMB = 1
EMPTY = 0
START_WIDTH = 16
START_HEIGHT = 10
START_BOMBS = 16
LEFT_MARGIN = 10
TOP_MARGIN = 10
LABEL_WIDTH = 4
LABEL_HEIGHT = 1


def start_new_game(field_width: int, field_height: int, bomb_count: int):
    """Настройка новой игры"""
    global bomb_matrix
    turn_count = 0
    field_ids = range(0, field_width * field_height)
    bomb_ids = random.sample(field_ids, bomb_count)
    bomb_matrix.clear()
    bomb_matrix.extend(list(EMPTY for _ in range(field_width))
                       for _ in range(field_height))
    for bomb in bomb_ids:
        bomb_matrix[bomb // field_width][bomb % field_width] = BOMB


def draw_game_controls():
    """Рисует элементы управления"""


def draw_counters():
    """Рисует счётчики флажков и времени"""


def draw_field(parent):
    """Рисует игровое поле"""
    w, h = len(bomb_matrix[0]), len(bomb_matrix)
    label_width = LABEL_WIDTH * 5
    label_height = LABEL_HEIGHT * 25
    win_w = LEFT_MARGIN * 2 + w * label_width
    win_h = TOP_MARGIN * 2 + h * label_height
    parent.geometry(f'{win_w}x{win_h}+100+100')
    for x in range(w):
        for y in range(h):
            text = '*' if bomb_matrix[y][x] == BOMB else '_'
            label = tkinter.Label(parent, text=text,
                width=LABEL_WIDTH, height=LABEL_HEIGHT)
            label.place(x=LEFT_MARGIN + x * label_width,
                        y=TOP_MARGIN + y * label_height)
            label.bind("<Button-1>", label_click)


def label_click(args):
    print(id(args.widget))


def configure(main_window):
    """Настройка основного окна"""
    draw_field(main_window)
    draw_game_controls()
    draw_counters()


if __name__ == "__main__":
    start_new_game(START_WIDTH, START_HEIGHT, START_BOMBS)
    master = tkinter.Tk()
    configure(master)
    master.mainloop()

