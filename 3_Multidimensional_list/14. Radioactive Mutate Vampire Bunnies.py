def create_lair(size):
    matrix = []
    for r in range(size):
        matrix.append(list(input()))

    return matrix


def escape(position, field):
    r, c = position
    if not (0 <= r < len(field) and 0 <= c < len(field[0])):
        return True
    return False


def next_cell(command, position, next_pos=None):
    row, col = position
    if command == "L":
        next_pos = (row, col - 1)
    elif command == "R":
        next_pos = (row, col + 1)
    elif command == "U":
        next_pos = (row - 1, col)
    elif command == "D":
        next_pos = (row + 1, col)

    return next_pos


def cell_in_lair(position, field):
    r, c = position
    return 0 <= r < len(field) and 0 <= c < len(field[0])


def spread(field, player_position_now):
    player_is_dead = False
    bunnies_positions = [
        (row, col)
        for row in range(len(field))
        for col in range(len(field[row]))
        if field[row][col] == "B"
    ]
    for bunny in bunnies_positions:
        bunny_row, bunny_col = bunny
        spread_cells = [
            (bunny_row, bunny_col + 1),
            (bunny_row, bunny_col - 1),
            (bunny_row + 1, bunny_col),
            (bunny_row - 1, bunny_col)
        ]
        for cell in spread_cells:
            if not cell_in_lair(cell, field):
                continue
            else:
                current_row, current_col = cell
                if field[current_row][current_col] == ".":
                    field[current_row][current_col] = "B"
                elif field[current_row][current_col] == "P":
                    player_is_dead = True
                    field[current_row][current_col] = "B"

    if player_is_dead:
        print_final_state_of_lair(field)
        print(f"dead: {player_position_now[0]} {player_position_now[1]}")
        exit(0)
    else:
        return field


def print_final_state_of_lair(field):
    [print(''.join(r)) for r in field]


rows, cols = [int(el) for el in input().split()]
lair = create_lair(rows)
directions = list(input())
player_position = [(row, col) for row in range(rows) for col in range(cols) if lair[row][col] == "P"]

current_position = (player_position[0][0], player_position[0][1])
while directions:
    current_command = directions.pop(0)
    next_position = next_cell(current_command, current_position)
    if escape(next_position, lair):
        lair[current_position[0]][current_position[1]] = "."
        lair = spread(lair, next_position)
        print_final_state_of_lair(lair)
        print(f"won: {current_position[0]} {current_position[1]}")
        exit(0)
    else:
        row, col = next_position
        current_cell = lair[row][col]
        if current_cell == ".":
            lair[current_position[0]][current_position[1]] = "."
            lair[row][col] = "P"
        elif current_cell == "B":
            lair = spread(lair, next_position)
            print_final_state_of_lair(lair)
            print(f"dead: {current_position[0]} {current_position[1]}")
            exit(0)
    lair = spread(lair, next_position)
    current_position = next_position
