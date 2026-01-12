from collections import deque
number_of_petrol_pumps = int(input())
petrol_tank = 0
pumps = deque()

for _ in range(number_of_petrol_pumps):
    car_fuel, car_distance = input().split()
    pumps.append({"fuel": int(car_fuel), "dist": int(car_distance)})


starting_position = 0
stops = 0

while stops < number_of_petrol_pumps:
    fuel = 0
    for i in range(number_of_petrol_pumps):
        fuel += pumps[i]["fuel"]
        distance = pumps[i]["dist"]
        if fuel < distance:
            pumps.rotate(-1)
            starting_position += 1
            stops = 0
            break
        fuel -= distance
        stops += 1

print(starting_position)