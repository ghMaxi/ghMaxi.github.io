import random

qs = ('Дайте определение модуля в Python и объясните работу команды импорта модуля.',
     'Дайте определение функции и поясните на примерах способы ей обмена данными с программой.',
     'Опишите четыре вида параметров функции и правила их применения с примерами.',
     'Опишите и приведите примеры ввода и вывода строк в консоль и внешние файлы.',
     '''Кратко опишите назначение следующих модулей Python:
  sys, os, os.path, shutil, tkinter, requests,
  socket, threading, json, csv, random''',
     'Дайте определение генератора и итератора в python и приведите примеры их работы',
     'Дайте определение класса и приведите пример класса в Python',
     'Дайте определение объекта и приведите пример, в котором Вы создаёте и применяете объект любого класса',
     'Опишите на примере жизненный цикл объекта в Python',
     'Дайте определения 4 основных принципов ООП и приведите пример класса, реализующего эти принципы в Python',
     'Напишите web-сервер, слушающий запросы по адресу localhost://index.html и возвращающий текст "ok"',
     'Напишите web-клиент, который при запуске запрашивает данные с адреса localhost://index.html и печатает результат',
     'Дайте определение 4 типов HTTP запросов и объясните их работу',
     'Приведите примеры описания одного и того же объекта на JSON и на XML',
     'Дайте определение многопоточности и напишите программу, в которой будут одновременно выполняться 2 цикла while(true)',
     '''Дайте определение реляционной БД.
Напишите программу, в которой в таблице users заводится запись об одном пользователе.
В записи должны быть автоматически увеличивающийся id и получаемые через запрос логин и пароль.''')
nums = list(range(len(qs)))


q_list = list([q, 6] for q in qs)
def get_random_3():
    new_selection = sorted(random.sample(range(len(q_list)), 3))
    dist = 4
    while new_selection[1] - new_selection[0] < dist or\
          new_selection[2] - new_selection[1] < dist or\
          q_list[new_selection[0]][1] == 0 or q_list[new_selection[1]][1] == 0 or q_list[new_selection[2]][1] == 0:
        new_selection = sorted(random.sample(nums, 3))
    for i in range(3): q_list[new_selection[i]][1] -= 1
    return '\n'.join(f'{qs[item]}' for i, item in enumerate(new_selection))


selection = set(get_random_3() for _ in range(30))
while len(selection) < 30:
    selection = set(get_random_3() for _ in range(30))
for line in sorted(selection):
    print(line, '\n')

