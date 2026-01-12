number_of_lines = int(input())
empty_stack = []
final_stack = []

for _ in range(number_of_lines):

    given_queri = input()

    if '1' in given_queri:
        given_queri = given_queri.split()
        num = int(given_queri[1])
        empty_stack.append(num)

    elif empty_stack:

        if given_queri == '2':
            if empty_stack:
                empty_stack.pop()

        elif given_queri == '3':
            print(max(empty_stack))

        elif given_queri == '4':
            print(min(empty_stack))

for n in range(len(empty_stack)):
    final_stack.append(str(empty_stack.pop()))

print(", ".join(final_stack))