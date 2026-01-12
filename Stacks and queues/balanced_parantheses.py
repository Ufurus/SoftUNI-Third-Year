given_parameters = input()

parentheses = {"(": ")", "[": "]", "{": "}"}
my_stack = []

for symbol in given_parameters:
    if symbol in parentheses:
        my_stack.append(symbol)
    elif symbol in parentheses.values():
        if not my_stack:
            print("NO")
            break
        last_opening = my_stack.pop()
        if parentheses[last_opening] != symbol:
            print("NO")
            break
else:
    if my_stack:
        print("NO")
    else:
        print("YES")