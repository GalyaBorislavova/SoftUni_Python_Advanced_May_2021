def check_valid_coord(check_matrix, r_1, c_1, r_2, c_2):
    if r_1 in range(len(check_matrix)) and r_2 in range(len(check_matrix)):
        if c_1 in range(len(matrix[0])) and c_2 in range(len(matrix[0])):
            return True

    return False


rows, cols = [int(el) for el in input().split()]

matrix = []

for r in range(rows):
    matrix.append([el for el in input().split()])

command = input().split()
while not command[0] == "END":
    if command[0] == "swap":
        if len(command) == 5:
            swap_command, *indexes = command
            row_1, col_1, row_2, col_2 = [int(el) for el in indexes]
            if check_valid_coord(matrix, row_1, col_1, row_2, col_2):
                matrix[row_1][col_1], matrix[row_2][col_2] = matrix[row_2][col_2], matrix[row_1][col_1]
                for row in range(rows):
                    print(*matrix[row])
            else:
                print("Invalid input!")
        else:
            print("Invalid input!")
    else:
        print("Invalid input!")
    command = input().split()