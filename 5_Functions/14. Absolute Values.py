numbers = input().split()

absolute_numbers = map(abs, [float(num) for num in numbers])

print(list(absolute_numbers))