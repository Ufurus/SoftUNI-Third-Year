import os

directory = "../"
files = {}

for file_name in os.listdir(directory):
    f = os.path.join(directory, file_name)

    if os.path.isfile(f):
        ext = file_name.split(".")[-1]
        if ext not in files:
            files[ext] = []
        files[ext].append(file_name)

    else:
        for el in os.listdir(f):
            filename = os.path.join(f, el)
            if os.path.isfile(filename):
                ext = el.split(".")[-1]
                if ext not in files:
                    files[ext] = []
                files[ext].append(el)

with open("report.txt", "w") as file:
    for ext, file_type in sorted(files.items()):
        file.write(f".{ext}\n")
        for name_file in sorted(file_type):
            file.write(f"- - - {name_file}\n")