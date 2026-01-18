n_rows = int(input())
matrix = []
for _ in range(n_rows):
    if matrix != []:
        matrix[0] += [int(x) for x in input().split(", ")]
    else:
        matrix.append([int(x) for x in input().split(", ")])

print(matrix[0])