rows = int(input())
my_matrix = []

first_diagonal = []
secondary_diagonal = []

for _ in range(rows):
    my_matrix.append([int(x) for x in input().split()])

for col in range(rows):
    first_diagonal.append(my_matrix[col][col])

for col in range(rows):
    secondary_diagonal.append(my_matrix[col][-col - 1])

total_sum = abs(sum(first_diagonal) - sum(secondary_diagonal))
print(total_sum)