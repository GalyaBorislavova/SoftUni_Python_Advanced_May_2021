from math import floor


def create_maze(size):
    matrix = []

    for _ in range(size):
        matrix.append([el for el in input().split()])

    return matrix


def cell_in_maze(current_row, current_col, maze):
    return 0 <= current_col < len(maze) and 0 <= current_row < len(maze)


def round_players_coins(coins):
    coins *= 0.5
    return floor(coins)


def check_cell(coord, maze, player_coins, path):
    row, col = [int(el) for el in coord]
    if not cell_in_maze(row, col, maze):
        win_coins = round_players_coins(player_coins)
        print(f"Game over! You've collected {win_coins} coins.")
        print("Your path:")
        for coord in player_path:
            print(f"[{', '.join([str(el) for el in coord])}]")
        exit(0)
    elif maze[row][col].upper() == "X":
        win_coins = round_players_coins(player_coins)
        print(f"Game over! You've collected {win_coins} coins.")
        print("Your path:")
        for coord in player_path:
            print(f"[{', '.join([str(el) for el in coord])}]")
        exit(0)
    elif maze[row][col].isdigit():
        player_coins += int(maze[row][col])

    return player_coins


n = int(input())
game_field = create_maze(n)
player_coord = [(r, c) for r in range(n) for c in range(n) if game_field[r][c] == "P"]
player_coord = (player_coord[0][0], player_coord[0][1])

total_coins_player = 0
player_path = []

current_move = input()
while True:

    if current_move == "up":
        next_player_coord = (player_coord[0] - 1, player_coord[1])
        total_coins_player = check_cell(next_player_coord, game_field, total_coins_player, player_path)
    elif current_move == "down":
        next_player_coord = (player_coord[0] + 1, player_coord[1])
        total_coins_player = check_cell(next_player_coord, game_field, total_coins_player, player_path)
    elif current_move == "left":
        next_player_coord = (player_coord[0], player_coord[1] - 1)
        total_coins_player = check_cell(next_player_coord, game_field, total_coins_player, player_path)
    elif current_move == "right":
        next_player_coord = (player_coord[0], player_coord[1] + 1)
        total_coins_player = check_cell(next_player_coord, game_field, total_coins_player, player_path)

    player_path.append([next_player_coord[0], next_player_coord[1]])
    player_coord = next_player_coord

    if total_coins_player >= 100:
        print(f"You won! You've collected {total_coins_player} coins.")
        print("Your path:")
        for coord in player_path:
            print(f"[{', '.join([str(el) for el in coord])}]")
        break

    current_move = input()
