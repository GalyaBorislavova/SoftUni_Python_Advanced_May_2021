import re
import sys


def player_points(player_1, player_2):
    points_dictionary = {player_1: 501, player_2: 501}

    return points_dictionary


def create_dartboard(size=7):
    matrix = []
    for r in range(size):
        matrix.append([el for el in input().split()])

    return matrix


def save_coord():
    pattern = r"[0-9]+"

    current_coord = input()
    current_row, current_col = re.findall(pattern, current_coord)
    current_row, current_col = int(current_row), int(current_col)

    return current_row, current_col


def coord_in_dartboard(row, col):
    return 0 <= row < 7 and 0 <= col < 7


def find_line_cells(board, row, col, double_or_triple):  # for double and triple result
    line_cells = [
        (row, 6),
        (row, 0),
        (0, col),
        (6, col),
    ]
    return calculate_point_for_double_and_triple_result(line_cells, board, double_or_triple)


def calculate_point_for_double_and_triple_result(line_cells, board, type_hit):
    sum_four_line_cells = 0
    for cell in line_cells:
        cell_row, cell_col = cell[0], cell[1]
        sum_four_line_cells += int(board[cell_row][cell_col])
    if type_hit == "D":
        return sum_four_line_cells * 2
    elif type_hit == "T":
        return sum_four_line_cells * 3


def is_winner(name, throws, result_dictionary):
    if result_dictionary[name] <= 0:
        print(f"{name} won the game with {throws} throws!")
        sys.exit(1)

    return False


def end_game(players_results):
    for player in players_results:
        if players_results[player] <= 0:
            return True

    return False


def game(dartboard, hit_cell, name, dictionary_points, throws):
    row, col = hit_cell
    if not coord_in_dartboard(row, col):
        return dictionary_points
    current_cell = dartboard[row][col]
    points = 0
    if current_cell.isdigit():
        points = int(dartboard[row][col])
    elif current_cell == "D":
        points = find_line_cells(dartboard, row, col, current_cell)
    elif current_cell == "T":
        points = find_line_cells(dartboard, row, col, current_cell)
    elif current_cell == "B":
        print(f"{name} won the game with {throws} throws!")
        sys.exit(1)

    dictionary_points[name] -= points

    if not is_winner(name, throws, dictionary_points):
        return dictionary_points


def main():
    name_first_player, name_second_player = [el for el in input().split(", ")]
    dartboard = create_dartboard()
    players_points = player_points(name_first_player, name_second_player)

    number_of_hits_for_first_player = 0
    number_of_hits_for_second_player = 0
    count = 0
    while not end_game(players_points):
        hit_coord = save_coord()
        count += 1
        if count % 2 == 1:
            number_of_hits_for_first_player += 1
            players_points = game(dartboard, hit_coord, name_first_player, players_points,
                                  number_of_hits_for_first_player)
        else:
            number_of_hits_for_second_player += 1
            players_points = game(dartboard, hit_coord, name_second_player, players_points,
                                  number_of_hits_for_second_player)


main()
