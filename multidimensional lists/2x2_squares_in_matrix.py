rows, columns = map(int, input().split())

my_matrix = []
identical_counter = 0

for _ in range(rows):
    my_matrix.append([x for x in input().split()])

for row in range(rows-1):
    for col in range(columns-1):
        current_element = my_matrix[row][col]
        next_element = my_matrix[row][col+1]
        below_element = my_matrix[row+1][col]
        diagonal_element = my_matrix[row+1][col+1]

        if current_element == next_element == below_element == diagonal_element:
            identical_counter += 1

print(identical_counter)
