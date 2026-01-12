from collections import deque
food_quantity = int(input())
given_orders = [int(num) for num in input().split()]
print(max(given_orders))

for i in given_orders:
    if i <= food_quantity:
        given_orders = deque(given_orders)
        food_quantity -= given_orders.popleft()
    else:
        break

if not given_orders:
    print("Orders complete")
else:
    given_orders = list(given_orders)
    print(f"Orders left:",*given_orders)
