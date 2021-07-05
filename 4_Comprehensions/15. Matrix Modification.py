def check_coord(row, col, matrix_with_numbers):
    return row in range(0, len(matrix_with_numbers)) and col in range(0, len(matrix_with_numbers[row]))


rows = int(input())

matrix = [[int(el) for el in input().split()] for r in range(rows)]

command = input()
while not command == "END":
    action, *action_data = command.split()
    row, col, value = [int(el) for el in action_data]
    if not check_coord(row, col, matrix):
        print("Invalid coordinates")
        command = input()
        continue
    if action == "Add":
        matrix[row][col] += value
    elif action == "Subtract":
        matrix[row][col] -= value

    command = input()


for r in matrix:
    print(*[el for el in r])

