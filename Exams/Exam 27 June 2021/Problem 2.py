def create_game_field(size):
    matrix = []
    coord = ()

    for row in range(size):
        row_data = input().split()
        if "A" in row_data:
            coord = (row, row_data.index("A"))
        matrix.append(row_data)

    return matrix, coord


def coord_in_field(row, col):
    return 0 <= row < 5 and 0 <= col < 5


def targets_in_field(game_field):
    return [1 for ind_row, row in enumerate(game_field) for el in row if el == "x"]


field, my_position = create_game_field(5)
n = int(input())

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}
hit_target_coord = []
success_movement = False

for _ in range(n):
    command, direction, *rest = input().split()

    if command == "move":
        steps = int(rest[0])
        desire_position_row = my_position[0] + directions[direction][0] * steps
        desire_position_col = my_position[1] + directions[direction][1] * steps

        if coord_in_field(desire_position_row, desire_position_col):
            if field[desire_position_row][desire_position_col] == ".":
                field[my_position[0]][my_position[1]] = "."
                my_position = desire_position_row, desire_position_col
                field[desire_position_row][desire_position_col] = "A"

    elif command == "shoot":
        target_row = my_position[0] + directions[direction][0]
        target_col = my_position[1] + directions[direction][1]

        while coord_in_field(target_row, target_col):
            if field[target_row][target_col] == "x":
                hit_target_coord.append([target_row, target_col])
                field[target_row][target_col] = "."
                break
            target_row += directions[direction][0]
            target_col += directions[direction][1]

    if not targets_in_field(field):
        break


targets = [1 for ind_row, row in enumerate(field) for ind_col, el in enumerate(row) if el == "x"]


if not targets and hit_target_coord:
    print(f"Training completed! All {len(hit_target_coord)} targets hit.")
if targets:
    print(f"Training not completed! {len(targets)} targets left.")

for coord in hit_target_coord:
    print(coord)


