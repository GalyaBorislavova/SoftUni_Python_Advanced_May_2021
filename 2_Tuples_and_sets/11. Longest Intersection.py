def input_to_list(count):
    lines = []
    for _ in range(count):
        line = input()
        if " " in line:
            data = line.split()
            for el in data:
                lines.append(el)
        else:
            lines.append(line)
    return lines


n = int(input())
input_sequences = input_to_list(n)

longest_intersection = set()
max_len_intersection = 0

for i in input_sequences:
    range_first_set, range_second_set = i.split("-")
    start_first_set, end_first_set = range_first_set.split(",")
    start_second_set, end_second_set = range_second_set.split(",")
    current_first_set = set(num for num in range(int(start_first_set), int(end_first_set) + 1))
    current_second_set = set(num for num in range(int(start_second_set), int(end_second_set) + 1))
    intersection = current_first_set.intersection(current_second_set)
    if len(intersection) > max_len_intersection:
        longest_intersection = intersection
        max_len_intersection = len(intersection)

print(f"Longest intersection is {[*longest_intersection]} with length {max_len_intersection}")





