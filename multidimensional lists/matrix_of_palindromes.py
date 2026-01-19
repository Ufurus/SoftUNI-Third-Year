rows, columns = [int(x) for x in input().split()]

start = ord("a")

for row in range(rows):
    for col in range(columns):
        print(f"{chr(start + row)}{chr(start + row + col)}{chr(start + row)}", end=" ")
    print()