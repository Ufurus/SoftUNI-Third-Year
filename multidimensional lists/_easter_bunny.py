field_size = int(input())
actual_field = [[x for x in input().split()] for _ in range(field_size)]

bunny_location = tuple()

for row in range(field_size):
    for col in range(field_size):
        if actual_field[row][col] == "B":
            bunny_location = (row, col)

possible_moves = {
    "down": (1, 0),
    "up": (-1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

max_eggs = float("-inf")
max_direction = ""
max_mat = []

for direction, move in possible_moves.items():
    eggs = 0
    curr_mat = []
    row = bunny_location[0] + move[0]
    col = bunny_location[1] + move[1]

    while 0 <= row < field_size and 0 <= col < field_size:
        if actual_field[row][col] == "X":
            break
        eggs += int(actual_field[row][col])
        curr_mat.append([row, col])
        row += move[0]
        col += move[1]

        if eggs > max_eggs and curr_mat:
            max_eggs = eggs
            max_direction = direction
            max_mat = curr_mat

print(max_direction)
[print(row) for row in max_mat]
print(max_eggs)