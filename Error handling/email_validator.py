class NameTooShortError(Exception):
    pass

class MustContainAtSymbolError(Exception):
    pass

class InvalidDomainError(Exception):
    pass

given_email = input()

while given_email != "End":

    if "@" in given_email:
        name = given_email[:given_email.index("@")]

        if len(name) <= 4:
            raise NameTooShortError("Name must be more than 4 characters")

    if "@" not in given_email:
        raise MustContainAtSymbolError("Email must contain @")

    if (given_email.endswith(".com") or given_email.endswith(".bg")
            or given_email.endswith(".org") or given_email.endswith(".net")):
        print("Email is valid")

    else:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    given_email = input()