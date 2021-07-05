def create_chess_board(size):
    matrix = []

    for row in range(size):
        matrix.append(input().split())

    return matrix


def find_king_position(game_board):
    king_coord = [(r, c) for r in range(len(game_board)) for c in range(len(game_board)) if game_board[r][c] == "K"]

    return king_coord[0]


def coord_in_board(row, col, matrix_size):
    return 0 <= row < matrix_size and 0 <= col < matrix_size


def find_which_queens_can_capture_king(game_board, king_coord):
    queen_coord = []
    king_row, king_col = king_coord
    directions = [
        (-1, 0),  # up
        (1, 0),  # down
        (0, -1),  # left
        (0, 1),  # right
        (-1, -1),  # left_up
        (-1, 1),  # right up
        (1, -1),  # left_down
        (1, 1)  # right_down
    ]
    for direction in directions:
        next_position_row = king_row + direction[0]
        next_position_col = king_col + direction[1]
        while coord_in_board(next_position_row, next_position_col, len(game_board)):
            if game_board[next_position_row][next_position_col] == "Q":
                queen_coord.append([next_position_row, next_position_col])
                break
            next_position_row = next_position_row + direction[0]
            next_position_col = next_position_col + direction[1]

    return queen_coord


def print_queens_coord(coord):
    if coord:
        for queen in coord:
            print(queen)
    else:
        print("The king is safe!")


def main():
    n = 8
    chess_board = create_chess_board(n)
    king_position = find_king_position(chess_board)
    capture_queens_coord = find_which_queens_can_capture_king(chess_board, king_position)
    print_queens_coord(capture_queens_coord)


main()
