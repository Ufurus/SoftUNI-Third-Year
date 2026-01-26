def operate(*args):
    numbers = []
    operator = ''
    for num in args:
        if not isinstance(num, int):
            operator = num
        else:
            numbers.append(int(num))

    if operator == "+":
        val = sum(numbers)
    elif operator == "*":
        val = 1
        for num in numbers:
            val = val * num
    elif operator == "-":
        val = numbers[0] - sum(numbers[1:])
    elif operator == "/":
        val = numbers[0]
        for num in numbers[1:]:
            val = val / num

    return val

print(operate("+", 1, 2, 3))
print(operate("/", 3, 4))