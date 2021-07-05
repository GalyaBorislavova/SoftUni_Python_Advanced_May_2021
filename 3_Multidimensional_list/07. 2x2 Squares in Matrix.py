rows, cols = [int(el) for el in input().split()]

matrix = []
count_matches = 0

for r in range(rows):
    matrix.append([el for el in input().split()])

for row in range(0, rows - 1):
    for col in range(0, cols - 1):
        top_left = matrix[row][col]
        top_right = matrix[row][col + 1]
        bottom_right = matrix[row + 1][col + 1]
        bottom_left = matrix[row + 1][col]
        if bottom_left == bottom_right == top_right == top_left:
            count_matches += 1

print(count_matches)