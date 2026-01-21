present_count = int(input())
n = int(input())
neighborhood_size = [[x for x in input().split()] for _ in range(n)]

santa_position = []
total_nice_kids = 0
nice_kid_count = 0

directions = {
    "down": (1, 0),
    "up": (-1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for row in range(n):
    for col in range(n):
        if neighborhood_size[row][col] == "S":
            santa_position = [row, col]
        elif neighborhood_size[row][col] == "V":
            total_nice_kids += 1

while present_count > 0:
    command = input()
    if command == "Christmas morning":
        break

    r, c = santa_position[0] + directions[command][0], santa_position[1] + directions[command][1]

    if 0 <= r < n and 0 <= c < n:
        if neighborhood_size[r][c] == "V":
            present_count -= 1
            nice_kid_count += 1
            neighborhood_size[r][c] = "-"
        elif neighborhood_size[r][c] == "C":
            for d in directions.values():
                next_r, next_c = r + d[0], c + d[1]
                if neighborhood_size[next_r][next_c] in "VX" and present_count > 0:
                    if neighborhood_size[next_r][next_c] == "V":
                        nice_kid_count += 1
                    present_count -= 1
                    neighborhood_size[next_r][next_c] = "-"

        neighborhood_size[santa_position[0]][santa_position[1]] = "-"
        santa_position = [r, c]
        neighborhood_size[r][c] = "S"

if present_count < 1 and nice_kid_count < total_nice_kids:
    print("Santa ran out of presents!")

[print(*row) for row in neighborhood_size]

if nice_kid_count < total_nice_kids:
    print(f"No presents for {total_nice_kids - nice_kid_count} nice kid/s.")
else:
    print(f"Good job, Santa! {nice_kid_count} happy nice kid/s.")