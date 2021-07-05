import sys

rows, cols = [int(el) for el in input().split(", ")]

matrix = []
max_sum = -sys.maxsize
position_right_bottom_element = None

for r in range(rows):
    matrix.append([int(el) for el in input().split(", ")])

for row in range(rows - 1, 0, -1):
    for col in range(cols - 1, 0, -1):
        current_sum = matrix[row][col] + matrix[row][col - 1] + matrix[row - 1][col] + matrix[row - 1][col - 1]
        if current_sum >= max_sum:
            position_right_bottom_element = (row, col)
            max_sum = current_sum


row_bottom, col_bottom = position_right_bottom_element

print(matrix[row_bottom - 1][col_bottom - 1], matrix[row_bottom - 1][col_bottom])
print(matrix[row_bottom][col_bottom - 1], matrix[row_bottom][col_bottom])
print(max_sum)
