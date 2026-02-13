def ship_movement(direction, position, matrix, resources):
    last_position = position
    rows, cols = position
    n = len(matrix)
    out_of_space = False
    mission_success = False
    if direction == "right":
        cols += 1
    elif direction == "left":
        cols -= 1
    elif direction == "up":
        rows -= 1
    elif direction == "down":
        rows += 1

    if 0 <= rows < n and 0 <= cols < n:
        resources -= 5
        if matrix[rows][cols] == 'M':
            resources -= 5
            matrix[rows][cols] = '.'
        elif matrix[rows][cols] == 'R':
            resources += 10
            if resources > 100:
                resources = 100
        elif matrix[rows][cols] == 'P':
            mission_success = True

    if not (0 <= rows < n) or not (0 <= cols < n):
        rows, cols = last_position
        out_of_space = True

    return (rows,cols), out_of_space, mission_success, resources

n = int(input())
matrix = [[x for x in input().split(' ')] for _ in range(n)]
resources = 100
ship_position = (0, 0)

for row in range(n):
    for col in range(n):
        if matrix[row][col] == 'S':
            ship_position = (row, col)
            matrix[row][col] = '.'

while True:

   ship_position, out_of_space, mission_success, resources = ship_movement(input(), ship_position, matrix, resources)

   if out_of_space:
       row, col = ship_position
       matrix[row][col] = 'S'
       print("Mission failed! The spaceship was lost in space.")
       break

   if mission_success:
       print(f"Mission accomplished! The spaceship reached Planet B with {resources} resources left.")
       break

   if resources < 5:
       row, col = ship_position
       matrix[row][col] = 'S'
       print("Mission failed! The spaceship was stranded in space.")
       break

for row in matrix:
    print(*row, sep=' ')