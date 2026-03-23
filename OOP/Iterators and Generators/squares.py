def squares(n: int):

    counter = 1
    num = 1
    while counter <= n:
        yield num
        counter += 1
        num = counter ** 2

print(list(squares(5)))