# каждый скрипт в Питоне это:
# 1) Выделенное пространство в памяти
# 2) Отдельный алгоритм работы с этой памятью
a = 10
print(a)
# Программирование на высоком уровне: создание пространств в памяти,
# отделённых друг от друга и выполняющих свои алгоритмы

# 3 основных подхода создания отдельных пространств памяти
# 1) функции
def my_function(param1, param2):
    # в момент вызова функции создаётся её собственное пространство в памяти
    result = param1 * param2
    print(param1, param2)

# Функциональная парадигма: подход к программированию, где
# высокий уровень программы достигается засчёт отдельных "чистых" функций

# Пример функционального подхода: питоновые сервера
# На питоновом сервере для каждого возможного способа взаимодействия пишется
# функция.
# Основной сервер на нашем курсе - flask

# 2) классы и объекты
# задача - создать в памяти компьютера устойчивую конфигурацию
# данных в нужных форматах
# класс задаёт конфигурацию данных

class ChessBoard:
    def __init__(self):
        self.cells = list([None]*8 for _ in range(8))
        self.place_figure(4, 0, "wK")

    def place_figure(self, x, y, name):
        self.cells[y][x] = name


# создание объекта принадлежащего классу
# 1) создаёт все данные в памяти согласно описанию класса
# 2) возвращает ссылку на положение этих данных в памяти
if __name__ == '__main__':
    chess_board = ChessBoard()
    chess_board.place_figure(0, 0, "wQ")
    chess_board2 = ChessBoard()
    chess_board2.place_figure(7, 7, "bQ")
    from pprint import pprint
    pprint(chess_board.cells)
    pprint(chess_board2.cells)

# Каждый объект является комбинацией конкретных данных этого объекта
# и общих для всех видов этих объектов процедур

