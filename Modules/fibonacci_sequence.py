from sequence.core import *

command = input()
sequence = None

while command != "Stop":
    num = int(command.split()[-1])

    if command.startswith("Create"):
        sequence = create_sequence(num)
        print(*sequence)

    elif command.startswith("Locate"):
        print(locate_number(num, sequence))

    command = input()