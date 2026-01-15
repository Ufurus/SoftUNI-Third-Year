first_sequence = set(int(x) for x in input().split())
second_sequence = set(int(x) for x in input().split())
number_of_lines = int(input())

for _ in range(number_of_lines):
    total_command = input().split()
    first_command = total_command[0]
    second_command = total_command[1]
    numbers = [int(x) for x in total_command[2:]]

    if first_command == "Add":
        if second_command == "First":
           first_sequence.update(numbers)
        elif second_command == "Second":
            second_sequence.update(numbers)
    elif first_command == "Remove":
        if second_command == "First":
            first_sequence.difference_update(numbers)
        elif second_command == "Second":
            second_sequence.difference_update(numbers)
    elif first_command == "Check":
        print(first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence))

print(*sorted(first_sequence), sep=", ")
print(*sorted(second_sequence), sep=", ")