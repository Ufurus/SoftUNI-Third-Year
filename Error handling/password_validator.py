class PasswordTooShortError(Exception):
    pass

class PasswordNoSpecialCharactersError(Exception):
    pass

class PasswordContainsSpacesError(Exception):
    pass

class PasswordTooCommonError(Exception):
    pass

special_chars = {"@", "*", "&", "%"}

def password_too_simple(pwd, specials):
    only_digits = pwd.isdigit()
    only_letters = pwd.isalpha()
    only_specials = all(ch in specials for ch in pwd)
    return only_digits or only_letters or only_specials

def special_character_check(pwd, specials):
    checker = False
    for el in pwd:
        if el in special_chars:
            checker = True
            break

    return checker

given_password = input()

while given_password != "Done":

    if len(given_password) < 8:
        raise PasswordTooShortError("Password must contain at least 8 characters")

    if password_too_simple(given_password, special_chars):
        raise PasswordTooCommonError("Password must be a combination of digits, letters, and special characters")

    if special_character_check(given_password, special_chars):
        pass
    else:
        raise PasswordNoSpecialCharactersError("Password must contain at least 1 special character")

    if " " in given_password:
        raise PasswordContainsSpacesError("Password must not contain empty spaces")

    print("Password is valid")
    given_password = input()