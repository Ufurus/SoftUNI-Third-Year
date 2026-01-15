from collections import deque
given_line = deque(input().split())

numbers = deque()
operations = {

    "*": lambda x, y: x * y,
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "/": lambda x, y: x // y

}

for char in given_line:
    if char not in "*+-/":
        numbers.append(int(char))
    else:
        while len(numbers) > 1:
            first_num = numbers.popleft()
            second_num = numbers.popleft()
            result = operations[char](first_num, second_num)
            numbers.appendleft(result)

print(*numbers)