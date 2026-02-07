from collections import deque

package_weight = [int(x) for x in input().split()]
courier_capacity = deque([int(x) for x in input().split()])

total_weight_delivered = 0

while package_weight and courier_capacity:

    current_package = package_weight[-1]
    current_courier = courier_capacity.popleft()

    if current_courier >= current_package:
        current_courier -= current_package * 2
        if current_courier > 0:
            courier_capacity.append(current_courier)
        total_weight_delivered += current_package
        package_weight.pop()

    else:
        package_weight[-1] -= current_courier
        total_weight_delivered += current_courier

print(f"Total weight: {total_weight_delivered} kg")

if not package_weight and not courier_capacity:
    print(f"Congratulations, all packages were delivered successfully by the couriers today.")

if package_weight and not courier_capacity:
    print(f"Unfortunately, there are no more available"
          f" couriers to deliver the following packages: {', '.join([str(x) for x in package_weight])}")

if courier_capacity and not package_weight:
    print(f"Couriers are still on duty:"
          f" {', '.join([str(x) for x in courier_capacity])} but there are no more packages to deliver.")