def find_sum_primary_diagonal(square_matrix):
    sum_diagonal = 0
    for r in range(len(square_matrix)):
        sum_diagonal += square_matrix[r][r]

    return sum_diagonal


size_matrix = int(input())

matrix = []

for row in range(size_matrix):
    matrix.append([int(el) for el in input().split()])

print(find_sum_primary_diagonal(matrix))