import random as rand


def spawn_location():
    row = lambda: rand.randint(0, 7 - 1)
    col = lambda: rand.randint(0, 7 - 1)

    spawn_a = [row(), col()]
    change = True
    while (change):
        spawn_o = [row(), col()]
        if spawn_o is not spawn_a:
            change = False

    print("ini psp" + str(spawn_a))
    print("ini psp" + str(spawn_o))
    print("ini return" + str(spawn_a + spawn_o))
    return spawn_a + spawn_o


def pawn_start(function):
    def wrapper():
        board = function()
        print("ini board" + str(board))
        spawn = spawn_location()
        board[spawn[0]][spawn[1]] = 'A'
        board[spawn[2]][spawn[3]] = 'O'
        return board

    return wrapper


@pawn_start
def board_size():
    return [['-' for i in range(7)] for i in range(7)]


def check_location(board, subject):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == subject:
                return [i, j]
    return 'not found'


def brakes(function):
    def wrapper(direction, board):
        present_location_a = check_location(board, 'A')
        try:
            movement = function(direction, board)
            for i in movement:
                if i < 0:
                    print("Melewati batas")
                    break
                else:
                    board[present_location_a[0]][present_location_a[1]] = '-'
                    board[movement[0]][movement[1]] = 'A'
                    return board
        except IndexError as err:
            print("warning melewati batas")
            print(err)
            board[present_location_a[0]][present_location_a[1]] = 'A'
        return board

    return wrapper


@brakes
def move(direction, board):
    location_A = check_location(board, 'A')
    row_a = location_A[0]
    column_b = location_A[1]

    if direction == 'up':
        return [row_a - 1, column_b]
    elif direction == 'down':
        return [row_a + 1, column_b]
    elif direction == 'right':
        return [row_a, column_b + 1]
    elif direction == 'left':
        return [row_a, column_b - 1]


def run():
    out = False

    board = board_size()
    location_o = check_location(board, 'O')

    while not out:

        print('* Selamat datang di Board Game Pemrograman Fungsional *')
        print('  anda (A) dapat berjalan secara horizontal maupun vertikal untuk menuju target (O)')
        print('  Selamat Bermain')

        for i in range(len(board)):
            for j in range(len(board[i])):
                print(board[i][j], end=' ')
            print()

        print('=========================')
        print('1. Cek Posisi')
        print('2. Geser Kanan')
        print('3. Geser Kiri')
        print('4. Geser Atas')
        print('5. Geser Bawah')
        print('6. Keluar')
        print('=========================')
        pilih = input('Pilihan: ')
        if pilih == '1':
            location_a = check_location(board, 'A')
            print(f'({location_a[0]}, {location_a[1]}')
        elif pilih == '2':
            move('right', board)
        elif pilih == '3':
            move('left', board)
        elif pilih == '4':
            move('up', board)
        elif pilih == '5':
            move('down', board)
        elif pilih == '6':
            out = True

        location_ab = check_location(board, 'A')
        if location_ab == location_o:
            print('Finish')
            out = True


run()
