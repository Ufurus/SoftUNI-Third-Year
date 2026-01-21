given_list = input().split("|")
my_matrix = []

for item in range(len(given_list) - 1, -1, -1):
      row = given_list[item].split()
      if row:
          my_matrix.append(row)

#[print(*j, sep=" ", end=" ") for j in my_matrix]

for row in my_matrix:
    print(*row, end=" ")