def movement(direction, position, total_health, given_grid, freeze):
    stars = 0
    rows, cols = position
    n = len(given_grid)
    if direction == "right":
        cols += 1
    elif direction == "left":
        cols -= 1
    elif direction == "up":
        rows -= 1
    elif direction == "down":
        rows += 1

    if (rows < 0 or rows >= n or cols < 0 or cols >= n) and matrix[rows % n][cols % n] == "*":
        stars += 1
        rows = rows % n
        cols = cols % n
        matrix[rows][cols] = "-"

    if (rows < 0 or rows >= n or cols < 0 or cols >= n) and matrix[rows % n][cols % n] == "F":
        rows = rows % n
        cols = cols % n
        freeze = True
        matrix[rows][cols] = "-"

    if (rows < 0 or rows >= n or cols < 0 or cols >= n) and matrix[rows % n][cols % n] == "G":
        rows = rows % n
        cols = cols % n
        if freeze:
            matrix[rows][cols] = "-"
            freeze = False
        else:
            total_health -= 50
        matrix[rows][cols] = "-"

    if (rows < 0 or rows >= n or cols < 0 or cols >= n) and matrix[rows % n][cols % n] == "-":
        rows = rows % n
        cols = cols % n
        matrix[rows][cols] = "-"

    if matrix[rows][cols] == "*":
        stars += 1
        matrix[rows][cols] = "-"

    if matrix[rows][cols] == "G":
        if freeze:
            matrix[rows][cols] = "-"
            freeze = False
        else:
            total_health -= 50
        matrix[rows][cols] = "-"

    if matrix[rows][cols] == "F":
        freeze = True
        matrix[rows][cols] = "-"

    return (rows, cols), stars, total_health, freeze

n = int(input())

matrix = []
health = 100
immunity = False
total_stars = 0
collected_stars = 0
pacman_position = (0, 0)

for row in range(n):
    x = list(input())
    matrix.append(x)

for row in range(n):
    for col in range(n):
        if matrix[row][col] == "P":
            pacman_position = (row, col)
            matrix[row][col] = "-"
        elif matrix[row][col] == "*":
            total_stars += 1

while True:

    command = input()
    if command == "end":
        break

    pacman_position, collected_star, health, freeze = movement(command, pacman_position, health, matrix, immunity)
    collected_stars += collected_star

    if collected_stars == total_stars:
        print(f"Pacman wins! All the stars are collected.")
        break

    if health <= 0:
        print(f"Game over! Pacman last coordinates [{row},{col}]")
        break

    if freeze:
        immunity = True
    else:
        immunity = False

if health > 0 and collected_stars < total_stars:
    print(f"Pacman failed to collect all the stars.")
print("Health:", health)
if collected_stars != total_stars:
    print("Uncollected stars:", total_stars - collected_stars)

row, col = pacman_position
matrix[row][col] = "P"
for row in matrix:
    print(''.join(row))