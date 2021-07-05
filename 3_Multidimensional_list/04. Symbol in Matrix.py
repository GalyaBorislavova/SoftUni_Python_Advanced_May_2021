size = int(input())

matrix = []
position = None

for r in range(size):
    matrix.append(list(input()))


symbol = input()

for row in range(size):
    for col in range(size):
        if matrix[row][col] == symbol:
            position = (row, col)
            break
    if position:
        break

print(position if position else f"{symbol} does not occur in the matrix")