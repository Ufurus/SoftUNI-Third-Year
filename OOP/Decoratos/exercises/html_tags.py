def tags(tag):
    def decorater(function):
        def wrapper(*args):
            result = function(*args)
            return f"<{tag}>{result}</{tag}>"
        return wrapper
    return decorater

@tags('p')
def join_strings(*args):
    return "".join(args)
print(join_strings("Hello", " you!"))


print()

@tags('h1')
def to_upper(text):
    return text.upper()
print(to_upper('hello'))
