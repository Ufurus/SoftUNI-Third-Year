def calculate(a: int, sign:str, b:int):
    result = 0
    if sign == "+":
        result =  a + b
    elif sign == "-":
        result = a - b
    elif sign == "*":
        result = a * b
    elif sign == "/":
        result = a / b
    elif sign == "^":
        result = a ** b

    return f"{result:.2f}"