square_size = int(input())
matrix = []
diagonal_sum = 0

for _ in range(square_size):
    matrix.append([int(x) for x in input().split()])

for j in range(square_size):
    diagonal_sum += matrix[j][j]

print(diagonal_sum)