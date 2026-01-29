file = open("numbers.txt", "r")

total_sum = 0

for n in file.read():
    if n.isdigit():
        total_sum += int(n)

print(total_sum)
file.close()