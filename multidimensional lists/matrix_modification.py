def coordinate_checker(r, l, row_n):
    return 0 <= r <= len(row_n) - 1 and 0 <= l <= len(row_n) - 1

rows = int(input())
my_matrix = [[int(x) for x in input().split()] for _ in range(rows)]

while True:

    for row_num in my_matrix:
        for col in range(rows):

            command = input()
            if command == "END":
                [print(*row) for row in my_matrix]
                exit()

            command = command.split()
            action = command[0]

            if action == "Add":

                row, col, value = int(command[1]), int(command[2]), int(command[3])
                checker = coordinate_checker(row, col, row_num)
                if checker:
                    my_matrix[row][col] += value
                else:
                    print("Invalid coordinates")

            elif action == "Subtract":

                row, col, value = int(command[1]), int(command[2]), int(command[3])
                checker = coordinate_checker(row, col, row_num)
                if checker:
                    my_matrix[row][col] -= value
                else:
                    print("Invalid coordinates")