health = 10
stress = 0
esteem = 5
family = 5

WIDTH = 25
divline = '-' * ((WIDTH + 1) * 4 + 1)
status_format_line = f'''{divline}
|{{:^{WIDTH}}}|{{:^{WIDTH}}}|{{:^{WIDTH}}}|{{:^{WIDTH}}}|
{divline}'''

CONTINUE = 0
EXIT = -1
game_status = CONTINUE
while game_status == CONTINUE:
    health_str = f'Здоровье: {health}'
    esteem_str = f'Успех: {esteem}'
    stress_str = f'Стресс: {stress}'
    family_str = f'Семья: {family}'
    print(status_format_line.format(health_str, esteem_str, stress_str, family_str))
    print("Описание ситуации")
    print(divline)
    print("Действия")
    max_choice = 0
    print(divline)
    choice = input(f"Ваш выбор ({EXIT} - выход): ")
    if choice == '0':
        game_status = EXIT
