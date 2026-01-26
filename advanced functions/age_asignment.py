def age_assignment(*names, **kwargs):
    name_list = [*names]
    result = sorted([])

    for letter, age in sorted(kwargs.items()):
        for name in name_list:
            if letter == name[0]:
                result.append(f"{name} is {age} years old.")

    return '\n'.join(result)

print(age_assignment("Peter", "George", G=26, P=19))

print("------------------------------")

print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))