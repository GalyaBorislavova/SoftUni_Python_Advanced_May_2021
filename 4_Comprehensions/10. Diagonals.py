def create_matrix(size_matrix):
    square_matrix = []
    for r in range(size_matrix):
        square_matrix.append([int(n) for n in input().split(", ")])

    return square_matrix


n = int(input())
matrix = create_matrix(n)
primary_diagonal = [matrix[i][i] for i in range(n)]
secondary_diagonal = [matrix[i][n - 1 - i] for i in range(n)]

print(f"First diagonal: {', '.join([str(n) for n in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
print(f"Second diagonal: {', '.join([str(n) for n in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")