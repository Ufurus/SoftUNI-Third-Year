import os
from constants import *

path_to_file = os.path.join(path_to_dir, "File handling", "text_n.txt")

symbols = {"-", ",", ".", "!", "?"}
lines = []

with open(path_to_file) as file:
    for line in file:
        a = line.split("\n")
        lines.append(a[0])

for li in lines:
    index = lines.index(li)
    for el in li:
        if el in symbols:
            li = li.replace(el, "@")
    lines[index] = li

for line in range(len(lines)):
    if line % 2 == 0:
        print(" ".join(lines[line].split()[::-1]))