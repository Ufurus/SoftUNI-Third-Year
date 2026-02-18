def draw(number):
    if number <= 0:
        return

    print("*" * number)

    draw(number - 1)

    print("#" * number)

draw(int(input()))