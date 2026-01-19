from collections import deque
n, m = map(int, input().split())
given_snake = deque(input())

my_matrix = [[str(x) for x in range(m)] for _ in range(n)]

for row in range(n):
    #my_matrix.append([""] * m)
    for col in range(m):
        if row % 2 == 0:
            my_matrix[row][col] = given_snake[0]
        else:
            my_matrix[row][-1 -col] = given_snake[0]
        given_snake.rotate(-1)

for item in my_matrix:
    print(*item, sep="")