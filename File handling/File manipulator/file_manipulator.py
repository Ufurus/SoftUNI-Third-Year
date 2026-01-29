import os

while True:

    command = input()
    if command == "End":
        break

    action, file_name, *args = command.split("-")

    if action == "Create":
        open(file_name, "w").close()

    elif action == "Add":
        with open(file_name, "a") as f:
            f.write(f"{args[0]}\n")

    elif action == "Replace":
        try:
            with open(file_name, "r+") as file:
                content = file.read()
                file.seek(0)
                file.truncate(0)
                file.write(content.replace(args[0], args[1]))
        except FileNotFoundError:
            print("An error occurred")

    elif action == "Delete":
        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            print("An error occurred")