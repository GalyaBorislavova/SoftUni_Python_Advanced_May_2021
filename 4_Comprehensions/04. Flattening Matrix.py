rows = int(input())

matrix = [int(num) for r in range(rows) for num in input().split(", ")]

print(matrix)