rows = int(input())
my_matrix = []

primary_diagonal = []
secondary_diagonal = []

for _ in range(rows):
    my_matrix.append([int(x) for x in input().split(", ")])

for col in range(rows):
    primary_diagonal.append(my_matrix[col][col])

for col in range(rows):
    secondary_diagonal.append(my_matrix[col][-col - 1])

print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")