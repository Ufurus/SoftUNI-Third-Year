def rectangle(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        return f"Enter valid values!"

    def area():
        return a * b
    def perimeter():
        return a * 2 + b * 2

    return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"

print(rectangle(2, 10))