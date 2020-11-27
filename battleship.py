import string
import os
import time


def init_board(board_range):
    os.system('cls' if os.name == 'nt' else 'clear')
    board = []
    for i in range(board_range):
        board.append([])
        for j in range(board_range):
            board[i].append("0")
    return board


def print_board(board, board_range, player):
    os.system('cls' if os.name == 'nt' else 'clear') 
    print("Player %s's turn." %player)
    print(" ", end=" ")
    for i in range(1, board_range+1):
        print(i, end=" ")
    print("")
    for i in range(board_range):
        print(string.ascii_uppercase[i], ' '.join(board[i]))


def valid_coord(player_coord):
    abc = ("abcdefghijklmnopqrstuvwxyz")
    valid_len = (2, 3)
    if len(player_coord) not in valid_len:
        print("Too long or too short word.")
        return (-1, -1)
    else:
        try:
            if len(player_coord) == 2:
                player_coord = (abc.index(player_coord[0]), (int(player_coord[1]) - 1))
                return player_coord
            else:
                player_coord = (abc.index(player_coord[0]), (int(player_coord[1] + player_coord[2]) - 1))
                return player_coord
        except:
            print("It's 2 or 3 letter string, not coordinate.")
            return (-1, -1)


def basic_coordinates(board):
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
                down = (board_coordinates[i][j])[0] + 1, (board_coordinates[i][j])[1]
                up = (board_coordinates[i][j])[0] - 1, (board_coordinates[i][j])[1]
                right = (board_coordinates[i][j])[0], (board_coordinates[i][j])[1] + 1
                left = (board_coordinates[i][j])[0], (board_coordinates[i][j])[1] - 1
                close_coordinates.append(down)
                close_coordinates.append(up)
                close_coordinates.append(right)
                close_coordinates.append(left)
    return ship_coordinates, close_coordinates, board_coordinates, board_all_coordinates


def get_placement(board):
    ship_coordinates, close_coordinates, board_coordinates, board_all_coordinates = basic_coordinates(board)
    while True:
        player_coord = (input("Add coordinate!" )).lower()
        player_coord = valid_coord(player_coord)
        if player_coord == (-1, -1):
            print("It's not valid coordinate.")
        elif player_coord in ship_coordinates:
            print("It's taken.")
        elif player_coord in close_coordinates:
            print("Ships are too close!")
        elif (player_coord not in board_all_coordinates) and (len(player_coord)) == 2 and player_coord != (-1, -1):
            print("Out of range.")
        else:
            break
    return player_coord


def select_direction(ship_1_part_coord, board):
    board_all_coordinates = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            board_all_coordinates.append((i, j))
    while True:
        valid_direction = ("horizontal", "vertical", "1", "2")
        direction = (input("Add direction! (horizontal[1]/vertical[2]) ")).lower()
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


def create_player_board(board_range, player):
    board = init_board(board_range)
    print("Player" + str(player) + "turn.")
    print_board(board, board_range, player)
    row, col = get_placement(board)
    mark(board, row, col)
    print_board(board, board_range, player)
    row, col = select_direction((row, col), board)
    mark(board, row, col)
    print_board(board, board_range, player)
    for shipmini in range(3):
        row, col = get_placement(board)
        mark(board, row, col)
        print_board(board, board_range, player)
    return board


def placement_phase(board_range):
    player = 1
    player1_board = create_player_board(board_range, player)
    #  wait
    # clear
    print("Next player's placement phase.")
    player = 2
    player2_board = create_player_board(board_range, player)
    # wait
    # clear
    return player1_board, player2_board


def twoboards(board, board2, board_range, player1, player2):
    width = 14
    if board_range == 6:
        width = 16
    if board_range == 7:
        width = 18
    if board_range == 8:
        width = 20
    if board_range == 9:
        width = 22
    if board_range == 10:
        width = 24
    print(player1, end=" ")
    print(player2.rjust(width))
    print("")
    print(" ", end=" ")
    for i in range(1, board_range+1):
        print(i, end=(" "))
    if board_range < 10:
        print("  ", end=" ")
        print(" ", end=" ")
    if board_range == 10:
        print("  ", end=" ")
    for i in range(1, board_range+1):
        print(i, end=(" "))
    print("")
    for i in range(board_range):
        print(string.ascii_uppercase[i],' '.join(board[i]),'  ',string.ascii_uppercase[i],' '.join(board2[i]))


def get_shooting(board):
    ship_coordinates, close_coordinates, board_coordinates, board_all_coordinates = basic_coordinates(board)
    while True:
        player_shooting_coord = (input("Add coordinate!")).lower()
        player_shooting_coord = valid_coord(player_shooting_coord)
        if player_shooting_coord == (-1, -1):
            print("It's not valid coordinate.")
        elif (player_shooting_coord not in board_all_coordinates) and (len(player_shooting_coord)) == 2 and player_shooting_coord != (-1, -1):
            print("Out of range.")
        else:
            break
    return player_shooting_coord


def check_ship_hit(board, player_shooting_coord, shooting_board):
    ship_coordinates, close_coordinates, board_coordinates, board_all_coordinates = basic_coordinates(board)
    miss_coord, hit_coord, sunk_coord = miss_hit_sunk_coord(shooting_board)
    if player_shooting_coord not in ship_coordinates:
        print("You've missed!")
        player_shooting_result = "M"
    else:
        print("You've hit a ship!")
        player_shooting_result = "H"
        # if player_shooting_coord
        #     print("You've sunk a ship!")
        #     player_shooting_result = "S"
    return player_shooting_result  # miss_hit_sunk


def miss_hit_sunk_coord(shooting_board):
    ship_coordinates, close_coordinates, board_coordinates, board_all_coordinates = basic_coordinates(shooting_board)
    miss_coord = []
    hit_coord = []
    sunk_coord = []
    for i in range(len(shooting_board)):
        for j in range(len(shooting_board[i])):
            if shooting_board[i][j] == "M":
                miss_coord.append(board_coordinates[i][j])
            elif shooting_board[i][j] == "H":
                hit_coord.append(board_coordinates[i][j])
            elif shooting_board[i][j] == "S":
                sunk_coord.append(board_coordinates[i][j])
    return miss_coord, hit_coord, sunk_coord


def has_won_player(board_range, board):
    how_many_are_sunk = 0
    for i in range(board_range):
        for j in range(board_range):
            if board[i][j] == "H":
                how_many_are_sunk += 1
    if how_many_are_sunk == 5:
        return True


def has_won(board_range, board1, board2):
    if has_won_player(board_range, board1) or has_won_player(board_range, board2):
        return True


def mark_shoot(board, row, col, miss_hit_sunk):
    board[row][col] = miss_hit_sunk


def shooting_phase(board_range, player1, player2, player1_board, player2_board):
    board = init_board(board_range)
    shooting_board_player1 = init_board(board_range)
    shooting_board_player2 = init_board(board_range)
    twoboards(shooting_board_player1, shooting_board_player2, board_range, player1, player2)
    while not has_won(board_range, shooting_board_player1, shooting_board_player2):
        print("Player1 turn.")
        player_shooting_coord = get_shooting(board)
        row, col = player_shooting_coord
        miss_hit_sunk = check_ship_hit(player2_board, player_shooting_coord, shooting_board_player2)
        mark_shoot(shooting_board_player2, row, col, miss_hit_sunk)
        twoboards(shooting_board_player1, shooting_board_player2, board_range, player1, player2)
        #########
        #os.system('cls' if os.name == 'nt' else 'clear')
        #########
        print("Player2 turn.")
        player_shooting_coord = get_shooting(board)
        row, col = player_shooting_coord
        miss_hit_sunk = check_ship_hit(player1_board, player_shooting_coord, shooting_board_player1)
        mark_shoot(shooting_board_player1, row, col, miss_hit_sunk)
        twoboards(shooting_board_player1, shooting_board_player2, board_range, player2, player1)
    winner = 0
    if has_won_player(board_range, shooting_board_player2):
        winner = 1
    elif has_won_player(board_range, shooting_board_player2):
        winner = 2
    print("Player" + str(winner) + " wins!")


def battle(board_range, player1, player2):
    player1_board, player2_board = placement_phase(board_range)
    shooting_phase(board_range, player1, player2, player1_board, player2_board)


def main_menu():
    print("B A T T L E S H I P")
    print("1.) Start Game\n2.) Customise board size\n3.) Quit Game\n")
    menu_option = input("")
    if menu_option == "1":
        print("Starting game . . .")
        time.sleep(1.65)
        os.system('cls' if os.name == 'nt' else 'clear')
        board_range = 5
        battle(board_range, "1", "2")
    elif menu_option == "2":
        print("Please give me the board size between 5 and 10;")
        board_range = int(input(""))
        if board_range > 10:
            correctrange = False
            while correctrange == False:
                print("Board is out of range!\nChoose a size between 5 and 10;")
                board_range = int(input(""))
                if board_range <= 10:
                    correctrange = True
        print("Starting game . . .")
        time.sleep(1.65)
        os.system('cls' if os.name == 'nt' else 'clear')
        battle(board_range, "1", "2")
    elif menu_option == "3":
        print("Goodbye!")
        exit()
    else:
        print("No other options.")
        time.sleep(1.65)
        os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    main_menu()

