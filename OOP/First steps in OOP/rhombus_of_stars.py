def upper_part(number):
    for row in range(1, number):
        print(" " * (number - row) + " *" * row)

def lower_part(number):
    for row in range(number, 0, -1):
        print(" " * (number - row) + " *" * row)

n = int(input())
upper_part(n)
lower_part(n)