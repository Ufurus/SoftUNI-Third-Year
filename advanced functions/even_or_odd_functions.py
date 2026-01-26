def even_odd(*args):

    args = list(args)
    command = ''

    for el in args:
        if type(el) != int:
            command = el
            args.pop()

    if command == "even":
        return [x for x in list(args) if x % 2 == 0]

    elif command == "odd":
        return [x for x in list(args) if x % 2 != 0]

print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))