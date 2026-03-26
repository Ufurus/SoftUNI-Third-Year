def type_check(given_type):
    def decorater(function):
        def wrapper(*args, **kwargs):
            if given_type == type(args[0]):
                result = function(*args, **kwargs)
                return result
            return "Bad Type"
        return wrapper
    return decorater

@type_check(int)
def times2(num):
    return num*2

print(times2(2))
print(times2('Not A Number'))

print()


@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
