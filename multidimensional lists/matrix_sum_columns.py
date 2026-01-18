rows, columns = map(int, input().split(", "))
matrix = []
total_sums = []
for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

for _ in range(columns):
    total_sums.append(0)

for j in range(columns):
    for row in matrix:
        total_sums[j] += row[j]

for n in total_sums:
    print(n, end="\n")