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

def win():
    if(game_field[0] == game_field[1] == game_field[2] or 
           game_field[3] == game_field[4] == game_field[5] or 
           game_field[6] == game_field[7] == game_field[8] or
           game_field[0] == game_field[3] == game_field[6] or
           game_field[1] == game_field[4] == game_field[7] or
           game_field[2] == game_field[5] == game_field[8] or
           game_field[0] == game_field[4] == game_field[8] or
           game_field[2] == game_field[4] == game_field[6]):
            print('Победил 1-ый игрок')
            return True

def player(mark):
    player_choice = int((input('Выберите номер ячейки: ')))
    if 1 <= player_choice <= 9:
        move(player_choice, mark)
        return win()
    else:
        print('Введено некорректное значение, повторите ввод')
        player()




# def first_player():
#     player_choice = int((input('Выберите номер ячейки: ')))
#     if 1 <= player_choice <= 9:
#         move(player_choice, mark = 'X')
#         return win()
#     else:
#         print('Введено некорректное значение, повторите ввод')
#         first_player()

# def second_player():
#     player_choice = int((input('Выберите номер ячейки: ')))
#     if 1 <= player_choice <= 9:
#         move(player_choice, mark = 'O')
#         win()
#     else:
#         print('Введено некорректное значение, повторите ввод')
#         second_player()

def game():
    mark = 'X'
    print_field()
    while True:
        if player(mark) == True:
            break
        if mark == 'X':
            mark = 'O'
        else:
            mark = 'X'
        

game()