import os
try:
    file = open("my_first_file.txt")
    file.close()
    os.remove("my_first_file.txt")
except FileNotFoundError:
    print("File already deleted")