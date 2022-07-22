game_field = [1, 4, 7, 2, 5, 8, 3, 6, 9]


def print_field():
    k = 0
    for i in range(1, 6):
        if (i in (1, 3, 5)):
            print(f'{game_field[k]}', ' | ', f'{game_field[k+3]}', ' | ',
                  f'{game_field[k+6]}')
            k += 1
        elif (i in (2, 4)):
            print('---|-----|----')

def move(choice,mark):
        game_field[game_field.index(choice)] = mark
        print_field()


def first_player():
    player_choice = int((input('Выберите номер ячейки: ')))
    if 1 <= player_choice <= 9:
        move(player_choice, mark = 'X')
    else:
        print('Введено некорректное значение, повторите ввод')
        first_player()

def second_player():
    player_choice = int((input('Выберите номер ячейки: ')))
    if 1 <= player_choice <= 9:
        move(player_choice, mark = 'O')
    else:
        print('Введено некорректное значение, повторите ввод')
        first_player()


print_field()
first_player()
second_player()
