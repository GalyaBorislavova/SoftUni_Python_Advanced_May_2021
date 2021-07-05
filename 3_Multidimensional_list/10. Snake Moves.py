rows, cols = [int(el) for el in input().split()]
snake = list(input())

matrix = [["" for c in range(cols)] for r in range(rows)]
index = 0
for row in range(rows):
    if row % 2 == 0:
        for c in range(cols):
            matrix[row][c] = snake[index]
            index += 1
            if index == len(snake):
                index = 0
    else:
        for c in range(cols - 1, -1, -1):
            matrix[row][c] = snake[index]
            index += 1
            if index == len(snake):
                index = 0

for sub in matrix:
    print("".join(sub))