try:
    file = open("text.txt", "r")
except FileNotFoundError:
    print("File not found")
else:
    print("File found")