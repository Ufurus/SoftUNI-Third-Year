n_row = int(input())
my_matrix = []
for row in range(n_row):
    my_matrix.append([x for x in input()])

symbol_to_find = input()
position = []

for row in range(n_row):
    for j in my_matrix[row]:
        if j == symbol_to_find:
            if position == []:
                position.append(row)
                position.append(my_matrix[row].index(j))

if position != []:
    print(f"({position[0]}, {position[1]})")
else:
    print(f"{symbol_to_find} does not occur in the matrix")