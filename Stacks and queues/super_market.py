from collections import deque
command = input()
customers = deque([])

while command != "End":

    if command == "Paid":
        for _ in deque(customers):
            print(customers.popleft())
    else:
        customers.append(command)
    command = input()

print(f"{len(customers)} people remaining.")