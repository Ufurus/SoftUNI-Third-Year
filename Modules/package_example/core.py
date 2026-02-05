def print_upper_row(n):
    for row in range(1, n+1):
        for num in range(1, row+1):
            print(num, end=" ")
        print()

def print_lower_row(n):
    for row in range(n-1, -1, -1):
        for num in range(1, row+1):
            print(num, end=" ")
        print()

def print_triangle(n):
    print_upper_row(n)
    print_lower_row(n)