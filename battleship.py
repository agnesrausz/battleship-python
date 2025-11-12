
def init_board(board_rows=5, board_cols=5):
    board = []
    for _ in range(board_rows):
        board.append(['0'] * board_cols)
    return board


def place_ship(board, row, col, direction, ship_size):
    pass


def get_ship_placement(board, player):
    pass
def get_ship_placement(board, ship_size):
    """Returns the coordinates of a valid ship placement on board."""
    first_letter_ascii_code = ord('a')
    row_len = len(board)
    col_len = len(board[0])

    while True:
        if ship_size == 1:
            placement = input(
                f'Enter your ship placement (e.g. B2): ').strip().lower().split()
            placement.append('h')  # default direction for size 1 ship
        else:
            placement = input(
                f'Enter your ship placement (e.g. B2 H for horizontal or C3 V for vertical): ').strip().lower().split()

        if len(placement[0]) != 2:
            print('Invalid coordinate, try again!')
            continue

        if not placement[0][0].isalpha() or not placement[0][1].isdigit():
            print('Invalid coordinate, try again!')
            continue

        if len(placement) != 2:
            print('Invalid input!')
            continue

        row = ord(placement[0][0]) - first_letter_ascii_code
        col = int(placement[0][1]) - 1
        direction = placement[1][0]

        if direction not in ['h', 'v']:
            print('Invalid direction, try again!')
            continue

        if not (0 <= row < row_len and 0 <= col < col_len):
            print('That move is out of bounds, try again!')
            continue

        coordinates = []
        for offset in range(ship_size):
            if direction == 'h':
                coordinates.append((row, col + offset))
            else:
                coordinates.append((row + offset, col))

        return coordinates


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_board(board):
    """Prints the board on the screen with borders."""
    clear()
    print('  ' + ' '.join(str(i + 1) for i in range(len(board[0]))))
    for i, row in enumerate(board):
        print(f'{chr(ord('A') + i)} ' + ' '.join(row))


if __name__ == "__main__":
    pass