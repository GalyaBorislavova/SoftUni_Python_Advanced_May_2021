command = input()
numbers = [int(x) for x in input().split()]

result = 0
if command == "Even":
    result = sum([x for x in numbers if x % 2 == 0])
elif command == "Odd":
    result = sum([x for x in numbers if x % 2 == 1])

print(result * len(numbers))