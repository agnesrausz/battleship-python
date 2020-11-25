import string


def init_board(board_range):
    board = []
    for i in range(board_range):
        board.append([])
        for j in range(board_range):
            board[i].append("0")
    return board


def print_board(board, board_range):
    print(" ", end=" ")
    for i in range(1, board_range+1):
        print(i, end=" ")
    print("")
    for i in range(board_range):
        print(string.ascii_uppercase[i], ' '.join(board[i]))


def valid_coord(player_coord):
    abc = ("abcdefghij")
    if not len(player_coord) == 2:
        print("It's not valid coordinate.")
        return (-1, -1)
    else:
        try:
            player_coord = (abc.index(player_coord[0]), (int(player_coord[1]) - 1))
            return player_coord
        except:
            print("ez dupla betű v szám")
            return (-1, -1)


def get_placement(board):
    row, col = 0, 0
    ship_coordinates = []
    close_coordinates = []
    board_coordinates = []
    board_all_coordinates = []
    out_of_range_coordinates = []
    for i in range(len(board) + 1):
        out_of_range_coordinates.append([])
        for j in range(len(board) + 1):
            out_of_range_coordinates[i].append((i, j))
    for i in range(len(board)):
        board_coordinates.append([])
        for j in range(len(board[i])):
            board_coordinates[i].append((i, j))
            board_all_coordinates.append((i, j))
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != "0":
                ship_coordinates.append(board_coordinates[i][j])
                close_coordinates.append(out_of_range_coordinates[i + 1][j])
                close_coordinates.append(out_of_range_coordinates[i - 1][j])
                close_coordinates.append(out_of_range_coordinates[i][j + 1])
                close_coordinates.append(out_of_range_coordinates[i][j - 1])
    while True:
        player_coord = (input("Add coordinate!")).lower()
        player_coord = valid_coord(player_coord)
        if player_coord == (-1, -1):
            print("ez nem jó")
        elif player_coord in ship_coordinates:
            print("I'ts taken.")
        elif player_coord in close_coordinates:
            print("Ships are too close!")
        elif (player_coord not in board_all_coordinates) and (len(player_coord)) == 2 and player_coord != (-1, -1):
            print("Out of range.")
        else:
            break
    row = player_coord[0]
    col = player_coord[1]
    return row, col


def select_direction(ship_1_part_coord, board):
    board_all_coordinates = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            board_all_coordinates.append((i, j))
    while True:
        valid_direction = ("horizontal", "vertical", "1", "2")
        direction = (input("Add direction! (horizontal[1]/vertical[2])")).lower()
        if direction not in valid_direction:
            print("It's not a valid direction")
        else:
            if direction == "horizontal" or direction == "1":
                if (ship_1_part_coord[0], ship_1_part_coord[1] + 1) not in board_all_coordinates:
                    ship_2_part_coord = (ship_1_part_coord[0], ship_1_part_coord[1] - 1)
                else:
                    ship_2_part_coord = (ship_1_part_coord[0], ship_1_part_coord[1] + 1)
                return ship_2_part_coord
            elif direction == "vertical" or direction == "2":
                if (ship_1_part_coord[0] + 1, ship_1_part_coord[1]) not in board_all_coordinates:
                    ship_2_part_coord = (ship_1_part_coord[0] - 1, ship_1_part_coord[1])
                else:
                    ship_2_part_coord = (ship_1_part_coord[0] + 1, ship_1_part_coord[1])
                return ship_2_part_coord


def mark(board, row, col):
    board[row][col] = "X"


if __name__ == "__main__":
    #  board_range = 5  # int(input("Please give me the board size:"))
    #  board = [['0','0','0','0','0'],['0','0','0','0','0'],['0','0','0','0','0'],['0','x','x','0','0'],['0','0','0','0','0']]
    #  print_board(board, board_range)
    board_range = 5
    board = init_board(board_range)
    print_board(board, board_range)
    print("Player 1 turn.")
    row, col = get_placement(board)
    mark(board, row, col)
    print_board(board, board_range)
    row, col = select_direction((row, col), board)
    mark(board, row, col)
    print_board(board, board_range)
    for shipmini in range(3):
        row, col = get_placement(board)
        mark(board, row, col)
        print_board(board, board_range)
