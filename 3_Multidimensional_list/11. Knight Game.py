def create_chess_board(size):
    matrix = []
    for _ in range(size):
        matrix.append([el for el in list(input())])

    return matrix


def knights_attacked_each_other(chess_board, all_knight_positions: list):
    for knight in all_knight_positions:
        knight_row, knight_col = knight

        attacked_positions = [
            (knight_row - 2, knight_col + 1),
            (knight_row - 1, knight_col + 2),
            (knight_row - 2, knight_col - 1),
            (knight_row - 1, knight_col - 2),
            (knight_row + 1, knight_col - 2),
            (knight_row + 1, knight_col + 2),
            (knight_row + 2, knight_col + 1),
            (knight_row + 2, knight_col - 1)
        ]
        for attack_position in attacked_positions:
            attack_row, attack_col = attack_position
            if not 0 <= attack_row < len(chess_board):
                continue
            if not 0 <= attack_col < len(chess_board):
                continue
            if chess_board[attack_row][attack_col] == "K":
                return True
    return False


def check_knight_positions(chess_board):
    positions = []
    for row in range(len(chess_board)):
        for col in range(len(chess_board[row])):
            if chess_board[row][col] == "K":
                positions.append((row, col))
    return positions


def check_aggression_score_of_every_knight(chess_board, positions):
    knight_aggressive_dictionary = {}
    for knight in positions:
        r, c = knight
        count_of_aggression = 0
        attacked_positions = [
            (r - 2, c + 1),
            (r - 1, c + 2),
            (r - 2, c - 1),
            (r - 1, c - 2),
            (r + 1, c - 2),
            (r + 1, c + 2),
            (r + 2, c + 1),
            (r + 2, c - 1)
        ]
        for attack_position in attacked_positions:
            attack_row, attack_col = attack_position
            if not 0 <= attack_row < len(chess_board):
                continue
            if not 0 <= attack_col < len(chess_board):
                continue
            if chess_board[attack_row][attack_col] == "K":
                count_of_aggression += 1
        knight_aggressive_dictionary[(r, c)] = count_of_aggression
    return knight_aggressive_dictionary


def most_aggressive_knight(aggression_dictionary):
    max_aggressive_knight_pos = tuple()
    max_aggressive_knight_score = None
    for pos, agg in aggression_dictionary.items():
        if max_aggressive_knight_score is None or (agg > max_aggressive_knight_score):
            max_aggressive_knight_score = agg
            max_aggressive_knight_pos = pos

    return max_aggressive_knight_pos


def main():
    size_board = int(input())
    board = create_chess_board(size_board)
    count_deleted_knights = 0
    while knights_attacked_each_other(board, check_knight_positions(board)) is True:
        knight_positions = check_knight_positions(board)
        aggression_scores = check_aggression_score_of_every_knight(board,
                                                                   knight_positions)
        row_to_delete, col_to_delete = most_aggressive_knight(aggression_scores)  # row, col

        # delete most_aggressive
        board[row_to_delete][col_to_delete] = "0"
        count_deleted_knights += 1
    print(count_deleted_knights)


main()
