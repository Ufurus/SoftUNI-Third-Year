from collections import deque

working_bees = deque(int(x) for x in input().split())
nectar = deque(int(x) for x in input().split())
symbol_sequence = deque(input().split())

collected_honey = 0

symbols = {

    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y if y != 0 else 0

}

while working_bees and nectar:

    current_bee = working_bees[0]
    current_nectar = nectar[-1]
    current_symbol = symbol_sequence[0]

    if nectar[-1] >= working_bees[0]:
        collected_honey += abs(symbols[current_symbol](current_bee, current_nectar))
        working_bees.remove(current_bee)
        nectar.remove(current_nectar)
        symbol_sequence.popleft()

    if current_nectar < current_bee:
        nectar.pop()

print(f"Total honey made: {collected_honey}")
if working_bees:
    print("Bees left: " + ", ".join(str(x) for x in working_bees))
if nectar:
    print("Nectar left: "+", ".join(str(x) for x in nectar))