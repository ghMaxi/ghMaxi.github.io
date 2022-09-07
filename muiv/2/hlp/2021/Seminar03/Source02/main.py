import tkinter
def make_field():
    return [[0, -1, 0],
            [-1, 0, 0],
            [0, 0, -1],
            [0, 0, -1]]


def get_height(matrix):
    return len(matrix)


def get_width(matrix):
    return len(matrix[0])


def is_bomb(matrix, row, col):
    return matrix[row][col] == -1


def bomb_count(matrix, _row, _col):
    count = 0
    for row in range(max(0, _row - 1),
                     min(_row + 2, get_height(matrix))):
        for col in range(max(0, _col - 1),
                         min(_col + 2, get_width(matrix))):
            if is_bomb(matrix, row, col):
                count += 1
    return count


def end_game(matrix, labels):
    for row in range(get_height(matrix)):
        for col in range(get_width(matrix)):
            labels[row][col].unbind("<Button-1>")
            if is_bomb(matrix, row, col):
                labels[row][col].configure(
                    text='*', relief='sunken')


def is_win(matrix):
    return all(
        0 not in row for row in matrix)


def open_field(matrix, row, col, labels):
    assert(not is_bomb(matrix, row, col))
    matrix[row][col] = 1
    number = bomb_count(matrix, row, col)
    if number == 0:
        pass
    labels[row][col].configure(
        text=f'{number}', relief='sunken')


def click(matrix, row, col, labels):
    if is_bomb(matrix, row, col):
        end_game(matrix, labels)
    else:
        open_field(matrix, row, col, labels)
        if is_win(matrix):
            print("YOU WIN")
            end_game(matrix, labels)


def make_function(matrix, row, col, labels):
    return lambda arg: click(
        matrix, row, col, labels)


def bind_key(matrix, row, col, labels):
    click_function = make_function(
        matrix, row, col, labels)
    labels[row][col].bind(
        "<Button-1>", click_function)


def new_label(row, col):
    BOX_SIZE = 25
    MARGIN = 10
    label = tkinter.Label(text=" ",
        height=1, width=2,
        borderwidth=2, relief="raised")
    label.place(y=row * BOX_SIZE + MARGIN,
                x=col * BOX_SIZE + MARGIN)
    return label


def make_labels(matrix):
    labels = []
    for row in range(get_height(matrix)):
        new_row = list()
        labels.append(new_row)
        for col in range(get_width(matrix)):
            label = new_label(row, col)
            new_row.append(label)
            bind_key(matrix, row, col, labels)


def make_window(matrix):
    window = tkinter.Tk()
    make_labels(matrix)
    return window


if __name__ == "__main__":
    play_field = make_field()
    play_window = make_window(play_field)
    play_window.mainloop()
