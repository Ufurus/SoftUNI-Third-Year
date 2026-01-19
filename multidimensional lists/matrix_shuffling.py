def zero_checker(r1, c1, r2, c2, row, col):
    return 0 <= r1 < row and 0 <= c1 < col and 0 <= r2 < row and 0 <= c2 < col

rows, columns = map(int, input().split())
my_matrix = [input().split() for _ in range(rows)]

while True:

    command = input()
    if command == "END":
        break

    command_check = command.split()

    if command_check[0] != "swap" or len(command_check) != 5:
         print("Invalid input!")
         continue

    first_row, first_col, second_row, second_col =\
        map(int, (command_check[1], command_check[2], command_check[3], command_check[4]))

    zero_check = zero_checker(first_row, first_col, second_row, second_col, rows, columns)

    if not zero_check:
        print("Invalid input!")
        continue

    a = my_matrix[first_row][first_col]
    b = my_matrix[second_row][second_col]

    my_matrix[first_row][first_col] = b
    my_matrix[second_row][second_col] = a
    [print(*row) for row in my_matrix]