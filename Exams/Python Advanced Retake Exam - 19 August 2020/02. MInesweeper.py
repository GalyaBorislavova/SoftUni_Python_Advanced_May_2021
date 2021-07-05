import re


def create_field(size_matrix):
    field = []
    for r in range(size_matrix):
        field.append([0] * size_matrix)

    return field


def check_bound(row_or_col, field):
    return 0 <= row_or_col < len(field)


def save_bomb_coord(bomb_number):
    bomb_coord = [] # [(row, col), (row, col)]
    pattern = r"[0-9]+"
    for bomb in range(bomb_number):
        current = input()
        result = re.findall(pattern, current)
        current_row, current_col = [int(el) for el in result]
        bomb_coord.append((current_row, current_col))

    return bomb_coord


def pin_bombs_on_field(field, bombs_coordinates):

    for row, col in bombs_coordinates:
        if check_bound(row, field) and check_bound(col, field):
            field[row][col] = "*"

    return field


def calculate_cell_number(field, size_filed):

    for r in range(size_filed):
        for c in range(size_filed):
            number = 0
            if field[r][c] != "*":
                adjacent_cells = [
                    (r - 1, c),
                    (r - 1, c + 1),
                    (r, c + 1),
                    (r + 1, c + 1),
                    (r + 1, c),
                    (r + 1, c - 1),
                    (r, c - 1),
                    (r - 1, c - 1)
                ]
                for pos in adjacent_cells:
                    current_row, current_col = pos
                    if not 0 <= current_row < len(field):
                        continue
                    if not 0 <= current_col < len(field):
                        continue
                    if field[current_row][current_col] == "*":
                        number += 1

                field[r][c] = number

    return field


def main():
    size = int(input())
    number_of_bombs = int(input())
    field_without_bombs = create_field(size)
    bomb_coord = save_bomb_coord(number_of_bombs)
    field_with_bombs = pin_bombs_on_field(field_without_bombs, bomb_coord)
    complete_field = calculate_cell_number(field_with_bombs, size)
    for r in complete_field:
        print(*r, sep=" ")


main()