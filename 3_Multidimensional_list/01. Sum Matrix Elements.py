rows, cols = [int(el) for el in input().split(", ")]

matrix = []
sum_elements = 0

for row in range(rows):
    current_row = [int(el) for el in input().split(", ")]
    sum_elements += sum(current_row)
    matrix.append(current_row)

print(sum_elements)
print(matrix)