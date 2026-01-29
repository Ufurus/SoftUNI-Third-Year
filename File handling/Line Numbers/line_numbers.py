from string import punctuation
line_number = 0

with open("text.txt") as file, open("output.txt", "w") as output_file:
    gathered_data = []
    for index, line in enumerate(file):
        letter_count = 0
        marks_count = 0

        for char in line:
            if char.isalpha():
                letter_count += 1
            elif char in punctuation:
                marks_count += 1

        gathered_data.append(f"Line {index + 1}: {line.strip()} ({letter_count})({marks_count})")

    output_file.write("\n".join(gathered_data))