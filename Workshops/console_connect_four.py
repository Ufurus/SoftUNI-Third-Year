def horizontal_winner(board):
    for row in range(6):
        first_player_col = 0
        second_player_col = 0
        for col in range(7):
            if board[row][col] == 1:
                first_player_col += 1
            elif board[row][col] == 2:
                second_player_col += 1
            else:
                break

        if first_player_col == 4 or second_player_col == 4:
            return True
    return False

def diagonal_winner(board):
    primary_diagonal_first_player = 0
    primary_diagonal_second_player = 0
    for r in range(len(board)):
        if board[r][r] == 1:
            primary_diagonal_first_player += 1
        elif board[r][r] == 2:
            primary_diagonal_second_player += 1

    if primary_diagonal_first_player == 4 or primary_diagonal_second_player == 4:
        return True

    col = 7
    secondary_diagonal_first_player = 0
    secondary_diagonal_second_player = 0
    for row_n in range(len(board)):
        col -= 1
        if board[row_n][col] == 1:
            secondary_diagonal_first_player += 1
        elif board[row_n][col] == 2:
            secondary_diagonal_second_player += 1

    if secondary_diagonal_first_player == 4 or secondary_diagonal_second_player == 4:
        return True

    return False

def vertical_winner(board):
    for col in range(7):
        first_player_col = 0
        second_player_col = 0
        for row in range(6):
            if board[row][col] == 1:
                first_player_col += 1
            elif board[row][col] == 2:
                second_player_col += 1
            else:
                break

        if first_player_col == 4 or second_player_col == 4:
            return True
    return False

def check_winner(board):
    is_horizontal_winner = horizontal_winner(board)
    is_vertical_winner = vertical_winner(board)
    is_diagonal_winner = diagonal_winner(board)

    if is_horizontal_winner or is_vertical_winner or is_diagonal_winner:
        return True
    return False

matrix = [[0 for x in range(7)] for _ in range(6)]
starting_player = 1

first_player_score = 0
second_player_score = 0

while True:

    current_player = "1" if starting_player % 2 != 0 else "2"
    print(f"Player {current_player}, please choose a column")
    try:
        chosen_column = int(input())

    except ValueError:
        print("Invalid column, please choose a valid one!")
        continue

    if chosen_column > 7 or chosen_column < 0:
        print("Invalid column, please choose a valid one!")
        continue

    current_col = chosen_column - 1
    current_row = chosen_column - 1

    for row in range(6):
        if matrix[row][current_col] == 0:
            matrix[row][current_col] = int(current_player)
            break
        else:
            try:
                while matrix[row][current_col] == 1 or matrix[row][current_col] == 2:
                    row += 1
                matrix[row][current_col] = int(current_player)
            except IndexError:
                print("Please choose another column! It is out of range")
            break

    for row in reversed(matrix):
        print(row)

    # if current_player == "1":
    #     first_player_score += 1
    # elif current_player == "2":
    #     second_player_score += 1
    #
    # if first_player_score > 4 == 0 or second_player_score > 4 == 0:
    if check_winner(matrix):
        print(f"The winner is player {current_player}")
        break

    starting_player += 1