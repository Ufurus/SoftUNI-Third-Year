from collections import deque
water_quantity = int(input())
line = input()
people = deque([]) # ['Bill', "Will"]

while line != "Start":

    people.append(line)
    line = input()

command = input()
while command != "End":

    if 'refill' not in command:
        command = int(command)

        if command <= water_quantity:
            print(f"{people.popleft()} got water")
            water_quantity -= command
        else:
            print(f"{people.popleft()} must wait")

    else:
        command = command.split()
        liters = int(command[1])
        water_quantity += liters

    command = input()

print(f"{water_quantity} liters left")