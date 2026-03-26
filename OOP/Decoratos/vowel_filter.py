def vowel_filter(function):

    filter_vowels = ['a', 'e', 'i', 'o', 'u']
    def wrapper():
        result = function()
        a = [x for x in result if x in filter_vowels]
        return a

    return wrapper

@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())