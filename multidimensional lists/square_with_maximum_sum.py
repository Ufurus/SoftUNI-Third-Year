rows, columns = map(int, input().split(", "))

found_submatrix = []
my_matrix = []
total_sum = 0

for _ in range(rows):
    my_matrix.append([int(x) for x in input().split(", ")])

for row in range(rows-1): #
    for col in range(columns-1):
        current_num = my_matrix[row][col] # 7
        next_num = my_matrix[row][col + 1] # 1
        below_num = my_matrix[row+1][col] # 1
        diagonal_num = my_matrix[row+1][col+1] # 3

        num_sum = current_num + next_num + below_num + diagonal_num
        if num_sum > total_sum:
            total_sum = num_sum
            found_submatrix = [[current_num, next_num], [below_num, diagonal_num]]


print(*found_submatrix[0])
print(*found_submatrix[1])
print(total_sum)