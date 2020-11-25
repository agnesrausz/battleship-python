import string, os
#Javítani:
#          a10 inputnál a1-et érzékel és oda rak

def init_board(board_range):
    board = []
    for i in range(board_range):
        board.append([])
        for j in range(board_range):
            board[i].append("0")
    return board

def init_board2(board_range):
    board2 = []
    for i in range(board_range):
        board2.append([])
        for j in range(board_range):
            board2[i].append("0")
    return board2


def print_board(board, board_range):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(" ", end=" ")
    for i in range(1, board_range+1):
        print(i, end=" ")
    print("")
    for i in range(board_range):
        print(string.ascii_uppercase[i], ' '.join(board[i]))

def print_board2(board2, board_range):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(" ", end=" ")
    for i in range(1, board_range+1):
        print(i, end=" ")
    print("")
    for i in range(board_range):
        print(string.ascii_uppercase[i], ' '.join(board2[i]))

def twoboards(board, board2):
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
    for i in range(1,board_range+1):
        print(i, end=(" "))
    if board_range < 10:
        print("  ", end=" ")
        print(" ", end=" ")
    if board_range == 10:
        print("  ", end=" ")
    for i in range(1,board_range+1):
        print(i, end=(" "))
    print("")
    for i in range(board_range):
        print(string.ascii_uppercase[i],' '.join(board[i]),'  ',string.ascii_uppercase[i],' '.join(board2[i]))


def valid_coord(player_coord):
    abc = ("abcdefghij")
    if board_range < 10:
        if not len(player_coord) == 2:
            #print("túl hosszú/nem helyes")
            return (-1, -1)
        else:
            try:
                player_coord = (abc.index(player_coord[0]), (int(player_coord[1]) - 1))
                return player_coord
            except:
                #print("ez dupla betű v szám")
                return (-1, -1)
    if board_range == 10:
        if not len(player_coord) == 3:
            #print("túl hosszú/nem helyes")
            return (-1, -1)
        else:
            try:
                player_coord = (abc.index(player_coord[0]), (int(player_coord[1]) - 1))
                return player_coord
            except:
                #print("ez dupla betű v szám")
                return (-1, -1)

def valid_coord2(player_coord_2):
    abc = ("abcdefghij")
    if board_range < 10:
        if not len(player_coord_2) == 2:
            #print("túl hosszú/nem helyes")
            return (-1, -1)
        else:
            try:
                player_coord_2 = (abc.index(player_coord_2[0]), (int(player_coord_2[1]) - 1))
                return player_coord_2
            except:
                #print("ez dupla betű v szám")
                return (-1, -1)
    if board_range == 10:
        if not len(player_coord_2) == 3:
            #print("túl hosszú/nem helyes")
            return (-1, -1)
        else:
            try:
                player_coord_2 = (abc.index(player_coord_2[0]), (int(player_coord_2[1]) - 1))
                return player_coord_2
            except:
                #print("ez dupla betű v szám")
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
        print("%s's turn."%player1)
        player_coord = (input("Add coordinate!\n")).lower()
        player_coord = valid_coord(player_coord)
        if player_coord == (-1, -1):
            print("Not a valid coordinate!")
        elif player_coord in ship_coordinates:
            print("It's taken.")
        elif player_coord in close_coordinates:
            print("Ships are too close!")
        elif (player_coord not in board_all_coordinates) and (len(player_coord)) == 2 and player_coord != (-1, -1):
            print("Out of range.")
        else:
            break
    row = player_coord[0]
    col = player_coord[1]
    
    return row, col

def get_placement2(board2):
    row2, col2 = 0, 0
    ship_coordinates2 = []
    close_coordinates2 = []
    board2_coordinates = []
    board2_all_coordinates = []
    out_of_range_coordinates = []
    for i in range(len(board2) + 1):
        out_of_range_coordinates.append([])
        for j in range(len(board2) + 1):
            out_of_range_coordinates[i].append((i, j))
    for i in range(len(board2)):
        board2_coordinates.append([])
        for j in range(len(board2[i])):
            board2_coordinates[i].append((i, j))
            board2_all_coordinates.append((i, j))
    for i in range(len(board2)):
        for j in range(len(board2[i])):
            if board2[i][j] != "0":
                ship_coordinates2.append(board2_coordinates[i][j])
                close_coordinates2.append(out_of_range_coordinates[i + 1][j])
                close_coordinates2.append(out_of_range_coordinates[i - 1][j])
                close_coordinates2.append(out_of_range_coordinates[i][j + 1])
                close_coordinates2.append(out_of_range_coordinates[i][j - 1])
    while True:
        print("%s's turn."%player2)
        player_coord2 = (input("Add coordinate!\n")).lower()
        player_coord2 = valid_coord2(player_coord2)
        if player_coord2 == (-1, -1):
            print("Not a valid coordinate!")
        elif player_coord2 in ship_coordinates2:
            print("It's taken.")
        elif player_coord2 in close_coordinates2:
            print("Ships are too close!")
        elif (player_coord2 not in board2_all_coordinates) and (len(player_coord2)) == 2 and player_coord2 != (-1, -1):
            print("Out of range.")
        else:
            break
    row2 = player_coord2[0]
    col2 = player_coord2[1]
    
    return row2, col2

def select_direction(ship_1_part_coord, board):
    board_all_coordinates = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            board_all_coordinates.append((i, j))
    while True:
        
        valid_direction = ("horizontal", "vertical", "1", "2")
        direction = (input("Add direction! (horizontal[1]/vertical[2])\n")).lower()
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
        
def select_direction2(ship_1_part_coord_p2, board2):
    board2_all_coordinates = []
    for i in range(len(board2)):
        for j in range(len(board2[i])):
            board2_all_coordinates.append((i, j))
    while True:
        
        valid_direction = ("horizontal", "vertical", "1", "2")
        direction = (input("Add direction! (horizontal[1]/vertical[2])\n")).lower()
        if direction not in valid_direction:
            print("It's not a valid direction")
        else:
            if direction == "horizontal" or direction == "1":
                if (ship_1_part_coord_p2[0], ship_1_part_coord_p2[1] + 1) not in board2_all_coordinates:
                    ship_2_part_coord = (ship_1_part_coord_p2[0], ship_1_part_coord_p2[1] - 1)
                else:
                    ship_2_part_coord = (ship_1_part_coord_p2[0], ship_1_part_coord_p2[1] + 1)
                return ship_2_part_coord
            elif direction == "vertical" or direction == "2":
                if (ship_1_part_coord_p2[0] + 1, ship_1_part_coord_p2[1]) not in board2_all_coordinates:
                    ship_2_part_coord = (ship_1_part_coord_p2[0] - 1, ship_1_part_coord_p2[1])
                else:
                    ship_2_part_coord = (ship_1_part_coord_p2[0] + 1, ship_1_part_coord_p2[1])
                return ship_2_part_coord

def mark(board, row, col):
    board[row][col] = "X"

def mark2(board2, row2, col2):
    board2[row2][col2] = "X"

if __name__ == "__main__":
    #  board_range = 5  # int(input("Please give me the board size:"))
    #  board = [['0','0','0','0','0'],['0','0','0','0','0'],['0','0','0','0','0'],['0','x','x','0','0'],['0','0','0','0','0']]
    #  print_board(board, board_range)

    player1 = input("Hello, what's your name, Player 1?\n")
    if player1 == "" or " ":
        player1 = "Player 1"
    player2 = input("Hello, what's your name, Player 2?\n")
    if player2 == "" or " ":
        player2 = "Player 2"
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Hi",player1,"and %s!" %player2)
    print("%s! Please give me the board size:"%player1)
    board_range = int(input (""))
    board = init_board(board_range)
    print_board(board, board_range)
    
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
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Next player's placement phase.")
    input("")
    board2 = init_board2(board_range)
    print_board2(board2, board_range)
    
    row2, col2 = get_placement2(board2)
    mark2(board2, row2, col2)
    print_board2(board2, board_range)
    row2, col2 = select_direction2((row2, col2), board2)
    mark2(board2, row2, col2)
    print_board2(board2, board_range)
    for shipmini2 in range(3):
        row2, col2 = get_placement2(board2)
        mark2(board2, row2, col2)
        print_board2(board2, board_range)

    os.system('cls' if os.name == 'nt' else 'clear')

    twoboards(board,board2)


