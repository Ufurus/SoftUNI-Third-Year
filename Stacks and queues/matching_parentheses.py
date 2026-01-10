given_line = input()
last_parentheses = []

for i in range(len(given_line)):
    if given_line[i] == "(":
        last_parentheses.append(i)
    elif given_line[i] == ")":
        starting_position = last_parentheses.pop()
        ending_position = i + 1
        print(given_line[starting_position:ending_position])