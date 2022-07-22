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



def win(id):
    if (game_field[0] == game_field[1] == game_field[2]
            or game_field[3] == game_field[4] == game_field[5]
            or game_field[6] == game_field[7] == game_field[8]
            or game_field[0] == game_field[3] == game_field[6]
            or game_field[1] == game_field[4] == game_field[7]
            or game_field[2] == game_field[5] == game_field[8]
            or game_field[0] == game_field[4] == game_field[8]
            or game_field[2] == game_field[4] == game_field[6]):
        print(f'Победил игрок №{id}')
        return True


def player(id):
    print(f'Ходит игрок №{id}')
    player_choice = int((input('Выберите номер ячейки: ')))
    if 1 <= player_choice <= 9:
        if id == 1:
            game_field[game_field.index(player_choice)] = 'X'
        else:
            game_field[game_field.index(player_choice)] = 'O'
        print_field()
        return win(id)
    else:
        print('Введено некорректное значение, повторите ввод')
        player(id)

def reset():
    global game_field
    answer = input(('Введите "Да", если желаете продожить игру'))
    if answer.upper() == 'ДА':
        game_field = [1, 4, 7, 2, 5, 8, 3, 6, 9]
        game()


def game():
    player_id = 1
    print_field()
    while True:
        if player(player_id) == True:
            break
        if player_id == 1:
            player_id = 2
        else:
            player_id = 1
    reset()
    


game()