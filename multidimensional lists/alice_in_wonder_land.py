n = int(input())
matrix = [[x for x in input().split()] for _ in range(n)]

alice_location = tuple()

for j in range(n):
    for i in range(n):
        if matrix[j][i] == "A":
            alice_location = (j, i)
            matrix[j][i] = "*"

collected_tea = 0

directions = {
    "down": (1, 0),
    "up": (-1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while collected_tea < 10:
    command = input()
    move = directions[command]
    row = alice_location[0] + move[0]
    col = alice_location[1] + move[1]

    if row < 0 or row >= n or col < 0 or col >= n:
        break
    if matrix[row][col] == "R":
        matrix[row][col] = "*"
        break

    if matrix[row][col] not in '.*':
        collected_tea += int(matrix[row][col])

    matrix[row][col] = "*"
    alice_location = (row, col)

if collected_tea < 10:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")

[print(*row) for row in matrix]