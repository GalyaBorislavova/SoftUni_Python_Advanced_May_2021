from collections import deque


def create_field(size):
    matrix = [[el for el in input().split()] for r in range(size)]

    return matrix


def is_valid_position(position, field_miner):
    row, col = position
    return 0 <= row < len(field_miner) and 0 <= col < len(field_miner)


def check_next_step(command, position):
    row, col = position
    next_pos = None
    if command == "left":
        next_pos = (row, col - 1)
    elif command == "right":
        next_pos = (row, col + 1)
    elif command == "up":
        next_pos = (row - 1, col)
    elif command == "down":
        next_pos = (row + 1, col)

    return next_pos


def check_cell(position, field_miner):
    r, c = position
    cell = field_miner[r][c]
    if cell == "*":
        pass
    elif cell == "c":
        field_miner[r][c] = "*"
    elif cell == "e":
        print(f"Game over! ({r}, {c})")
        exit(0)

    return field_miner


def check_all_coals_is_collected(field_miner):
    coals_position = [
        1
        for r in range(len(field_miner))
        for c in range(len(field_miner))
        if field_miner[r][c] == "c"
    ]
    if not coals_position:
        return True
    return False


def check_number_of_left_coals(field_miner, number_left_coals=0):
    for r in range(len(field_miner)):
        for c in range(len(field_miner)):
            if field_miner[r][c] == "c":
                number_left_coals += 1

    return number_left_coals


n = int(input())
commands = deque([el for el in input().split()])
field = create_field(n)
start_position = [(r, c) for r in range(n) for c in range(n) if field[r][c] == "s"]

current_position = (start_position[0][0], start_position[0][1])
while commands:
    current_command = commands.popleft()
    next_position = check_next_step(current_command, current_position)
    if not is_valid_position(next_position, field):
        continue
    else:
        field = check_cell(next_position, field)
        if check_all_coals_is_collected(field):
            print(f"You collected all coals! ({next_position[0]}, {next_position[-1]})")
            exit(0)
    current_position = next_position

print(f"{check_number_of_left_coals(field)} coals left. ({current_position[0]}, {current_position[-1]})")

