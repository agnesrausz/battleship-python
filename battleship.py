import os
import sys


def init_board(board_rows=5, board_cols=5):
    """Initializes and returns an empty board."""
    board = []
    for _ in range(board_rows):
        board.append(['0'] * board_cols)
    return board


def place_ship(board, coordinates):
    """Places a ship on the board."""
    for row, col in coordinates:
        board[row][col] = 'X'
    return board


def is_valid_coordinates(board, coordinates):
    return True


def is_space_free(board, coordinates):
    """Checks if the space for the ship is free and not adjacent to other ships."""
    row_len = len(board)
    col_len = len(board[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for row, col in coordinates:
        # Check the ship's coordinates
        if board[row][col] != '0':
            return False
        # Check adjacent coordinates
        for dr, dc in directions:
            adj_row, adj_col = row + dr, col + dc
            if 0 <= adj_row < row_len and 0 <= adj_col < col_len:
                if board[adj_row][adj_col] != '0':
                    return False
    return True


def get_ship_placement(board, ship_size):
    """Returns the coordinates of a valid ship placement on board."""
    first_letter_ascii_code = ord('a')
    row_len = len(board)
    col_len = len(board[0])

    while True:
        # if ship_size == 1:
        #     placement = input(
        #         f'Enter your ship placement (e.g. B2): ').strip().lower().split()
        #     if 'h' or 'v' not in placement:
        #         placement.append('h')  # default direction for size 1 ship
        # else:
        #     placement = input(
        #         f'Enter your ship placement (e.g. B2 H for horizontal or C3 V for vertical): ').strip().lower().split()

        placement = input(
            f'Enter your ship placement (e.g. B2 H for horizontal or C3 V for vertical): ').strip().lower().split()

        if len(placement) != 2:
            print('Invalid input, try again!')
            continue

        if len(placement[0]) != 2:
            print('Invalid coordinate, try again!')
            continue

        if not placement[0][0].isalpha() or not placement[0][1].isdigit():
            print('Invalid coordinate, try again!')
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

        if ((direction == 'h' and col + ship_size > col_len) or
                (direction == 'v' and row + ship_size > row_len)):
            print('Ship does not fit on the board, try again!')
            continue

        coordinates = []
        for offset in range(ship_size):
            if direction == 'h':
                coordinates.append((row, col + offset))
            else:
                coordinates.append((row + offset, col))

        if not is_space_free(board, coordinates):
            print('Ship is in the way or ships are too close, try again!')
            continue

        return coordinates


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_board(board):
    """Prints the board on the screen with borders."""
    clear()
    print('  ' + ' '.join(str(i + 1) for i in range(len(board[0]))))
    for i, row in enumerate(board):
        print(f'{chr(ord('A') + i)} ' + ' '.join(row))


def print_boards(board_player1, board_player2):
    """Prints both players' boards side by side."""
    clear()
    print('    Player 1          Player 2')
    print('  ' + ' '.join(str(i + 1) for i in range(len(board_player1[0]))) + '     ' +
          '  ' + ' '.join(str(i + 1) for i in range(len(board_player2[0]))))
    for i in range(len(board_player1)):
        row_label = chr(ord('A') + i)
        row_player1 = ' '.join(board_player1[i])
        row_player2 = ' '.join(board_player2[i])
        print(f'{row_label} {row_player1}   {row_label} {row_player2}')


def wait_for_keypress():
    if os.name == "nt":
        import msvcrt
        msvcrt.getch()
    else:
        import termios
        import tty
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)


def placement_phase(ships_to_place):
    board = init_board()
    for ship_size in ships_to_place:
        print_board(board)
        ship_placement = get_ship_placement(board, ship_size)
        board = place_ship(board, ship_placement)
    print_board(board)
    return board


def get_shot(board):
    """Returns the coordinates of a valid shot."""
    first_letter_ascii_code = ord('a')
    row_len = len(board)
    col_len = len(board[0])

    while True:
        shot = input('Enter your shot (e.g. B2): ').strip().lower()

        if len(shot) != 2:
            print('Invalid coordinate, try again!')
            continue

        if not shot[0].isalpha() or not shot[1].isdigit():
            print('Invalid coordinate, try again!')
            continue

        row = ord(shot[0]) - first_letter_ascii_code
        col = int(shot[1]) - 1

        if not (0 <= row < row_len and 0 <= col < col_len):
            print('That shot is out of bounds, try again!')
            continue

        if board[row][col] != '0' and board[row][col] != 'X':
            print('You already shot that coordinate, try again!')
            continue

        return row, col


def mark_shrunk_ship(board, row, col):
    # ai - not tested
    """Marks the ship as sunk if all parts are hit."""
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    ship_cells = [(row, col)]

    # Find all parts of the ship
    for dr, dc in directions:
        r, c = row + dr, col + dc
        while 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] in ['X', 'H']:
            ship_cells.append((r, c))
            r += dr
            c += dc

    # Check if all parts are hit
    if all(board[r][c] == 'H' for r, c in ship_cells):
        for r, c in ship_cells:
            board[r][c] = 'S'



def battleship():
    ships_to_place = [2, 1]  # Example ship sizes
    board_player1 = placement_phase(ships_to_place)
    clear()
    print('Next player\'s placement phase. Press any key to continue...')
    wait_for_keypress()
    board_player2 = placement_phase(ships_to_place)


if __name__ == "__main__":
    battleship()
