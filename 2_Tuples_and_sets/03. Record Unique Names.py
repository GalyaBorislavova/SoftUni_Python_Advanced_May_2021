def input_to_list(count):
    lines = []
    for _ in range(count):
        line = input()
        lines.append(line)
    return lines


n = int(input())
input_names = input_to_list(n)

unique_names = set(input_names)
for name in unique_names:
    print(name)