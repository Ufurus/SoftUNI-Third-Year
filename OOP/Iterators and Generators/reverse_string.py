def reverse_text(text: str):
    start_index = -1

    while abs(start_index) <= len(text):
        yield text[start_index]
        start_index -= 1

for char in reverse_text("step"):
    print(char, end='')