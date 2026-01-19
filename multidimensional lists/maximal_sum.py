rows, columns = map(int, input().split())

my_matrix = []
total_sum = -float("inf")
max_row = 0
max_col = 0

for _ in range(rows):
    my_matrix.append([int(x) for x in input().split()])

for row in range(rows - 2):
    for col in range(columns - 2):
        current_sum = 0
        for r in range(row, row + 3):
            for c in range(col, col + 3):
                current_sum += my_matrix[r][c]

        if current_sum > total_sum:
            total_sum = current_sum
            max_row = row
            max_col = col

print(f"Sum = {total_sum}")
max_submatrix = [my_matrix[r][max_col:max_col + 3] for r in range(max_row, max_row + 3)]
[print(*row) for row in max_submatrix]
