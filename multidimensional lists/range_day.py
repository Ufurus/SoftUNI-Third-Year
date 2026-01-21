SIZE = 5

range_size = [[x for x in input().split()] for _ in range(SIZE)]
number_of_commands = int(input())

player_position = []
target_hits = 0
target_location = []
available_targets = 0

for row in range(5):
    for col in range(5):
        if range_size[row][col] == "A":
            player_position = [row, col]

for row_n in range(5):
    for col_n in range(5):
        if range_size[row_n][col_n] == "x":
            available_targets += 1

directions = {
    "down": (1, 0),
    "up": (-1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for _ in range(number_of_commands):

    given_command = input().split()
    action = given_command[0]
    direction = given_command[1]

    if action == "shoot":
        row = player_position[0] + directions[direction][0]
        col = player_position[1] + directions[direction][1]

        while 0 <= row < SIZE and 0 <= col < SIZE:
            if range_size[row][col] == "x":
                target_location.append([row,col])
                range_size[row][col] = "."
                available_targets -= 1
                target_hits += 1
                break
            row += directions[direction][0]
            col += directions[direction][1]
        if available_targets == 0:
            print(f"Training completed! All {target_hits} targets hit.")
            [print(row) for row in target_location]
            break

    elif action == "move":
        steps = int(given_command[2])
        row = player_position[0] + directions[direction][0] * steps
        col = player_position[1] + directions[direction][1] * steps

        if 0 <= row < SIZE and 0 <= col < SIZE:
            if range_size[row][col] == ".":
                range_size[row][col] = "A"
                range_size[player_position[0]][player_position[1]] = "."
                player_position = [row, col]

if available_targets > 0:
    print(f"Training not completed! {available_targets} targets left.")
    [print(row) for row in target_location]
