numbers = input().split()

round_numbers = map(round, [float(num) for num in numbers])

print(list(round_numbers))