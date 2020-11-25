import string
board_range = int(input (""))
board = []

def init_board(board_range):
    for i in range(board_range):
        board.append([])
        for j in range(board_range):
            board[i].append("0")
    return board

def print_board(board):
    for i in range(1,board_range+1):
        print(" ",i, end=" ")
    print("")
    for i in range(board_range):
        print(string.ascii_uppercase[i],board[i])


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
    for i in range(len(board)):
        board_coordinates.append([])
        for j in range(len(board[i])):
            board_coordinates[i].append((i, j))
            board_all_coordinates.append((i, j))
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != "0":
                ship_coordinates.append(board_coordinates[i][j])
                close_coordinates.append(board_coordinates[i + 1][j])
                close_coordinates.append(board_coordinates[i - 1][j])
                close_coordinates.append(board_coordinates[i][j + 1])
                close_coordinates.append(board_coordinates[i][j - 1])
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


def mark(board, row, col):
    board[row][col] = "X"

if __name__ == "__main__":
    board = init_board(board_range)
    get_placement(board)
