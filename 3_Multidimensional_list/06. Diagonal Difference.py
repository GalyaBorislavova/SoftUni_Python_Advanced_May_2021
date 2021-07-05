size = int(input())

matrix = []
primary_diagonal = 0
secondary_diagonal = 0

for r in range(size):
    matrix.append([int(el) for el in input().split()])

for row in range(size):
    primary_diagonal += matrix[row][row]

row_count = 0
for col in range(size - 1, -1, -1):
    secondary_diagonal += matrix[row_count][col]
    row_count += 1

print(abs(primary_diagonal - secondary_diagonal))