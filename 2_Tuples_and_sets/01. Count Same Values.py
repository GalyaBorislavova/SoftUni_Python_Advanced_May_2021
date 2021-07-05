numbers = [float(num) for num in input().split(" ")]

occurrences = {}

for n in numbers:
    if n not in occurrences:
        occurrences[n] = 0
    occurrences[n] += 1

for (key, value) in occurrences.items():
    print(f"{key} - {value} times")