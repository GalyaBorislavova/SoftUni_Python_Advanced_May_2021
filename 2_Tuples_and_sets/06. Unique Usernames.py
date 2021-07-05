def input_to_list(count):
    lines = []
    for _ in range(count):
        line = input()
        lines.append(line)
    return lines


def add_unique_name(names):
    unique = set()
    for name in names:
        if name not in unique:
            unique.add(name)
    return unique


def print_unique_names(names):
    for name in names:
        print(name)


n = int(input())
input_names = input_to_list(n)

unique_names = add_unique_name(input_names)
print_unique_names(unique_names)

