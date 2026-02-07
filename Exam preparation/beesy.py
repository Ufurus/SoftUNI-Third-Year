n = int(input())

matrix = []
total_energy = 15
energy_restored = False
min_amount_of_nectar = 30
collected_nectar = 0

bee_r, bee_c = 0, 0

for row in range(n):
    matrix.append(list(input()))
    for col in range(n):
        if matrix[row][col] == 'B':
            bee_r, bee_c = row, col
            matrix[row][col] = "-"

def move_bee_position(direction, r, c):
    if direction == 'down':
        r = (r + 1) % n
    elif direction == 'up':
        r = (r - 1) % n
    elif direction == 'right':
        c = (c + 1) % n
    elif direction == 'left':
        c = (c - 1) % n

    return r, c

while True:
    total_energy -= 1
    bee_r, bee_c = move_bee_position(input(), bee_r, bee_c)

    if matrix[bee_r][bee_c].isdigit():
        collected_nectar += int(matrix[bee_r][bee_c])
        matrix[bee_r][bee_c] = "-"

    if matrix[bee_r][bee_c] == "H":
        if collected_nectar >= min_amount_of_nectar:
            print(f"Great job, Beesy! The hive is full. Energy left: {total_energy}")
        else:
            print(f"Beesy did not manage to collect enough nectar.")
        break

    if total_energy <= 0:
        if not energy_restored and collected_nectar >= min_amount_of_nectar:
            total_energy = collected_nectar - min_amount_of_nectar
            energy_restored = True
            collected_nectar = min_amount_of_nectar
        else:
            print(f"This is the end! Beesy ran out of energy.")
            break

matrix[bee_r][bee_c] = "B"
for row in matrix:
    print("".join(row))