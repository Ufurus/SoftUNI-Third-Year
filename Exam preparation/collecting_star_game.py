def check_position(command, pos, matrix):
    rows, cols = pos
    n = len(matrix)
    if command == "right":
        cols += 1
    elif command == "left":
        cols -= 1
    elif command == "up":
        rows -= 1
    elif command == "down":
        rows += 1

    if (rows < 0 or rows >= n or cols < 0 or cols >= n) and matrix[0][0] == "*":
        matrix[0][0] = "."
        return (0, 0), 1
    if (rows < 0 or rows >= n or cols < 0 or cols >= n):
        return (0, 0), 0
    if matrix[rows][cols] == "#":
        return pos, -1
    if matrix[rows][cols] == "*":
        matrix[rows][cols] = "."
        return (rows, cols), 1

    return (rows, cols), 0

field_size = int(input())
matrix = [[x for x in input().split()] for _ in range(field_size)]

total_stars = 2
player_position = (0, 0)

for row in range(field_size):
    for col in range(field_size):
        if matrix[row][col] == "P":
            player_position = (row, col)
            matrix[row][col] = "."

while True:

    player_position, star_change = check_position(input(), player_position, matrix)
    total_stars += star_change

    if total_stars >= 10:
        print("You won! You have collected 10 stars.")
        break
    if total_stars <= 0:
        print("Game over! You are out of any stars.")
        break

final_row, final_col = player_position
matrix[final_row][final_col] = "P"

print(f"Your final position is [{final_row}, {final_col}]")
for row in matrix:
    print(" ".join(row))