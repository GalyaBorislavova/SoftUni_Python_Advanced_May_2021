with open("text") as file:
    lines = file.readlines()

symbols = ["-", ",", ".", "!", "?"]

for ind, line in enumerate(lines):
    if ind % 2 == 0:
        for el in symbols:
            line = line.replace(el, "@").strip()

        line_as_list = [word for word in line.split()]
        print(' '.join(list(reversed(line_as_list))))


