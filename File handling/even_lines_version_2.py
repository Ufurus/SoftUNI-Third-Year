with open("text_n.txt", "r") as file:
    for index, line in enumerate(file):
        if index % 2 == 0:
            for el in "-,.!?":
                line = line.replace(el, "@")
            print(" ".join(reversed(line.split())))