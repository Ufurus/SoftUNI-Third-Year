from itertools import permutations

def possible_permutations(items: list):

    perm = permutations(items)
    for i in perm:
        yield list(i)

[print(n) for n in possible_permutations([1, 2, 3])]