from string import ascii_letters


def coord_in_field(row, col, n):
    return 0 <= row < n and 0 <= col < n


def game(game_field, player, turns, my_string):
    letters = []
    directions = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }
    for command in turns:
        next_player_row = player[0] + directions[command][0]
        next_player_col = player[1] + directions[command][1]
        if coord_in_field(next_player_row, next_player_col, len(game_field)):
            game_field[player[0]][player[1]] = "-"
            cell = game_field[next_player_row][next_player_col]
            if cell in ascii_letters:
                letters.append(cell)
            game_field[next_player_row][next_player_col] = "P"
            player = next_player_row, next_player_col
        else:
            if letters:
                letters.pop()
            else:
                if my_string:
                    my_string.pop()
            next_player_row -= directions[command][0]
            next_player_col -= directions[command][1]

    return game_field, letters, my_string


def print_result(initial, add_letters):
    initial = ''.join(initial)
    if add_letters:
        add_letters = ''.join(add_letters)
        print(initial + add_letters)
    else:
        print(initial)


def print_field(game_field):
    for row in game_field:
        print(''.join(row))


def main():
    initial_string_as_list = list(input())
    n = int(input())
    field = [list(input()) for r in range(n)]
    m = int(input())
    turns = [input() for t in range(m)]
    player_coord = [(row, col) for row in range(len(field)) for col in range(len(field)) if field[row][col] == "P"]
    field, add_string, initial_string_as_list = game(field, player_coord[0], turns, initial_string_as_list)
    print_result(initial_string_as_list, add_string)
    print_field(field)


main()

