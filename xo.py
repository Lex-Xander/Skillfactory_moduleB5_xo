def game_field(f):
    num = '  0 1 2'
    print(num)
    for row, i in zip(f, num.split()):
        print(f"{i} {' '.join(str(j) for j in row)}")

def players_input(f,player):
    while True:
        step = input(f"{player} - Введите координаты:").split()
        if len(step) != 2:
            print('Введите две координаты')
            continue

        if not(step[0].isdigit() and step[1].isdigit()):
            print('Введите числа')
            continue
        x, y = map(int, step)
        if not(x >= 0 and x < 3 and y >= 0 and y < 3):
            print('Ошибочный ввод')
            continue
        if f[x][y] != '-':
            print('Эта клетка уже занята')
            continue
        break
    return x, y

def victory(f, player):
    game_list = []
    print(f)
    for L in f:
        game_list += L
    print(game_list)
    positions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    indexes = set([i for i, x in enumerate(game_list) if x == player])

    for p in positions:
        if len(indexes.intersection(set(p))) == 3:
            return True
    return False

def start(field):
    count = 0
    while True:
        game_field(field)
        if count % 2 == 0:
            player = 'x'
        else:
            player = 'o'
        if count < 9:
            x, y = players_input(field, player)
            field[x][y] = player

        elif count == 9:
            print('Ничья')
            break
        if victory(field, player):
            print(f"Выйграл {player}")
            break
        count += 1

field = [['-'] * 3 for _ in range(3)]

start(field)
