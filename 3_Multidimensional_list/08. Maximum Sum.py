import sys

rows, cols = [int(el) for el in input().split()]

matrix = []
max_sum = -sys.maxsize
coord_max_top_left_element = tuple()

for r in range(rows):
    matrix.append([int(el) for el in input().split()])

for row in range(0, rows - 2):
    for col in range(0, cols - 2):
        top_left: int = matrix[row][col]
        top_middle: int = matrix[row][col + 1]
        top_right: int = matrix[row][col + 2]
        mid_left: int = matrix[row + 1][col]
        mid_middle: int = matrix[row + 1][col + 1]
        mid_right: int = matrix[row + 1][col + 2]
        bottom_left: int = matrix[row + 2][col]
        bottom_middle: int = matrix[row + 2][col + 1]
        bottom_right: int = matrix[row + 2][col + 2]
        current_3_x_3_matrix = (
        top_right, top_middle, top_left, mid_right, mid_middle, mid_left, bottom_middle, bottom_right, bottom_left)
        current_sum_elements = sum(current_3_x_3_matrix)
        if current_sum_elements > max_sum:
            coord_max_top_left_element = row, col
            max_sum = current_sum_elements

start_row, start_col = coord_max_top_left_element
print(f"Sum = {max_sum}")
print(f"{matrix[start_row][start_col]} {matrix[start_row][start_col + 1]} {matrix[start_row][start_col + 2]}")
print(
    f"{matrix[start_row + 1][start_col]} {matrix[start_row + 1][start_col + 1]} {matrix[start_row + 1][start_col + 2]}")
print(
    f"{matrix[start_row + 2][start_col]} {matrix[start_row + 2][start_col + 1]} {matrix[start_row + 2][start_col + 2]}")
