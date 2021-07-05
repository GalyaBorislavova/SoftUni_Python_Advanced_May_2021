import os

line = input()
while not line == "End":
    command, *command_data = line.split("-")

    if command == "Add":
        file_name, line = command_data
        with open(file_name, "a") as file:
            file.write(line + "\n")
    elif command == "Create":
        with open(command_data[0], "w"):
            pass
    elif command == "Delete":
        try:
            os.remove(command_data[0])
        except FileNotFoundError:
            print("An error occurred")
    elif command == "Replace":
        file_name, old_string, new_string = command_data
        try:
            with open(file_name, "r") as file:
                file_content = file.read()
                file_content = file_content.replace(old_string, new_string)

            with open(file_name, "w") as file:
                file.write(file_content)
        except Exception:
            print("An error occurred")

    line = input()
