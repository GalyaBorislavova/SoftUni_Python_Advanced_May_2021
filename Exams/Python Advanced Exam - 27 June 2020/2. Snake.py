def create_territory_and_find_snake_coord_and_burrows(size):
    matrix = []
    snake_coord = ()
    burrows_coord = []

    for row in range(size):
        row_data = list(input())
        if "S" in row_data:
            snake_coord = (row, row_data.index("S"))
        if "B" in row_data:
            burrow_col = [ind for ind, el in enumerate(row_data) if el == "B"][0]
            burrows_coord.append((row, burrow_col))
        matrix.append(row_data)

    if burrows_coord:
        return matrix, snake_coord, burrows_coord[0], burrows_coord[1]
    else:
        return matrix, snake_coord


def cell_in_territory(row, col, len_territory):
    return 0 <= row < len_territory and 0 <= col < len_territory


def game():
    n = int(input())
    territory, snake_position, *burrows = create_territory_and_find_snake_coord_and_burrows(n)

    food_quantity = 0
    directions = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }
    while True:
        command = input()
        snake_row, snake_col = snake_position
        next_snake_row = snake_row + directions[command][0]
        next_snake_col = snake_col + directions[command][1]

        if not cell_in_territory(next_snake_row, next_snake_col, len(territory)):
            print("Game over!")
            print(f"Food eaten: {food_quantity}")
            territory[snake_row][snake_col] = "."
            [print(''.join(row)) for row in territory]
            exit(0)
        else:
            current_cell = territory[next_snake_row][next_snake_col]
            if current_cell == "B":
                other_burrow = [coord for coord in burrows if (next_snake_row, next_snake_col) != coord][0]
                next_snake_row = other_burrow[0]
                next_snake_col = other_burrow[1]
                for coord in burrows:
                    current_row, current_col = coord
                    territory[current_row][current_col] = "."
            elif current_cell == "*":
                food_quantity += 1

        territory[snake_row][snake_col] = "."
        snake_position = next_snake_row, next_snake_col
        territory[next_snake_row][next_snake_col] = "S"

        if food_quantity >= 10:
            print("You won! You fed the snake.")
            print(f"Food eaten: {food_quantity}")
            [print(''.join(row)) for row in territory]
            exit(0)


game()
