with open("text") as file:
    lines = file.readlines()

for ind, line in enumerate(lines):
    characters = 0
    symbols = 0
    for el in line.replace(" ", "").strip():
        if el.isalnum():
            characters += 1
        else:
            symbols += 1
    print(f"Line {ind + 1}: {line.strip()} ({characters})({symbols})")

