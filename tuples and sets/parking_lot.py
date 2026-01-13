number_of_commands = int(input())
parking_lot = set()
for n in range(number_of_commands):
    action = input().split(", ")
    direction, car_number = action

    if direction == "IN":
            parking_lot.add(car_number)

    elif direction == "OUT":
            parking_lot.remove(car_number)

if parking_lot:
    for car in parking_lot:
        print(car)
else:
    print("Parking Lot is Empty")