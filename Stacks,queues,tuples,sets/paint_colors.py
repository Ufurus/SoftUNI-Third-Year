from collections import deque
given_string = deque(input().split())

main_colors = ['red', 'yellow', 'blue']
secondary_colors = {"orange": ["red", "yellow"],
                    "purple": ["red", "blue"],
                    "green": ["yellow", "blue"]}
found_colors = []

while given_string:

    first_string = given_string.popleft()
    second_string = given_string.pop() if given_string else ""

    for element in (first_string + second_string, second_string + first_string):
        if element in main_colors or element in secondary_colors:
            found_colors.append(element)
            break

    else:
        if len(first_string) > 1:
            given_string.insert(len(given_string) // 2, first_string[:-1])
        if len(second_string) > 1:
            given_string.insert(len(given_string) // 2, second_string[:-1])



for color in found_colors:
    if color in secondary_colors:
        for el in secondary_colors[color]:
            if el not in found_colors:
                found_colors.remove(color)
                break

print(found_colors)
