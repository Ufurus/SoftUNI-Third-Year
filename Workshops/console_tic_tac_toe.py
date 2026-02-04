def check_row(board, sign):
    for row in board:
        if row.count(sign) == 3:
            return True
    return False

def check_col(board,sign):
    for col in range(3):
        counter = 0
        for row in range(3):
            if board[row][col] == sign:
                counter += 1
        if counter == 3:
            return True
    return False

def check_diagonal(board, sign):
    primary_diagonal_counter = 0
    for i in range(3):
        if board[i][i] == sign:
            primary_diagonal_counter += 1

    second_diagonal_count = 0
    for j in range(2, -1, -1):
        if board[j][j] == sign:
            second_diagonal_count += 1

    if primary_diagonal_counter == 3 or second_diagonal_count == 3:
        return True
    return False

def check_for_winner(board, player, sign):
    is_row_winner = check_row(board,sign)
    is_col_winner = check_col(board, sign)
    is_diagonal_winner = check_diagonal(board, sign)

    if is_row_winner or is_diagonal_winner or is_col_winner:
        return True
    return False

def print_board(board):
    for row in board:
        print(f"| {' | '.join(row)} |")

player_one_name = input("Player one name: ")
player_two_name = input("Player two name: ")
player_one_sign = input(f"{player_one_name} would you like play with 'X' or 'O'? ").upper()
matrix = [[" ", " ", " "] for _ in range(3)]

mapper = {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    7: (2, 0),
    8: (2, 1),
    9: (2, 2)
}

while player_one_sign not in ["X", "O"]:
    print("Please enter a valid symbol! 'X' or 'O'.")
    player_one_sign = input(f"{player_one_name} would you like play with 'X' or 'O'? ").upper()

player_two_sign = "O" if player_one_sign == "X" else "X"

print("This is the numeration of the board:")

for i in range(1, 10):
    print(f"|  {i}  ", end="" if i % 3 != 0 else "|\n")

print(f"{player_one_name} starts first!")

turn = 1

while turn < 10:

    current_player = player_one_name if turn % 2 != 0 else player_two_name
    current_sign = player_one_sign if turn % 2 != 0 else player_two_sign
    try:
        position = int(input(f"{current_player} choose a free position [1-9]: "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    if position not in range(1, 10):
        print("Please enter a valid number, between 1-9!")
        continue

    row, col = mapper[position]
    if matrix[row][col] != " ":
        print("This position is already occupied")
        continue

    matrix[row][col] = f"{current_sign}"

    if turn >= 5 and check_for_winner(matrix, current_player, current_sign):
        print(f"{current_player} won!")
        break
    turn += 1
    print_board(matrix)

else:
    print("No winners today! Thanks for playing")