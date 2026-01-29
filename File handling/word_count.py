import os
import re
from constants import *

needed_words = []
data = {}

path_to_words = os.path.join(path_to_dir, "File handling", "words.txt")
path_to_input = os.path.join(path_to_dir, "File handling", "input.txt")

with open(path_to_words) as file:
    needed_words = file.read().split()

with open(path_to_input) as second_file:
    text = second_file.read()

for word in needed_words:
    pattern = rf"\b{word}\b"
    matches = re.findall(pattern, text, re.IGNORECASE)
    data[word] = len(matches)

ordered_data = sorted(data.items(), key=lambda x: -x[1])

with open(os.path.join(path_to_dir, "File handling","output.txt"), "w") as file:
    for word, times in ordered_data:
        file.write(f"{word} - {times}\n")

with open("output.txt") as file:
    print(file.read())