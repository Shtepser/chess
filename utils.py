def notation_to_indexes(notation: str):
    if len(notation) != 2:
        raise ValueError(f"{notation} is not a valid square position"
                          " in chess notation")
    file, rank = notation
    col = ord(file) - ord('A')
    row = int(rank) - 1
    if not (0 <= row <= 7 and 0 <= col <= 7):
        raise ValueError(f"{notation} is not a valid square position"
                          " in chess notation")
    return row, col


def indexes_to_notation(row: int, col: int):
    return f"{col_to_file(col)}{row + 1}"


def col_to_file(col: int):
    return chr(ord('A') + col)


def on_same_file(first_square, second_square):
    return first_square[0] == second_square[0]


def on_same_rank(first_square, second_square):
    return int(first_square[1]) == int(second_square[1])


def on_same_diagonal(first_square, second_square):
    first_row, first_col = notation_to_indexes(first_square)
    second_row, second_col = notation_to_indexes(second_square)
    return abs(first_row - second_row) == abs(first_col - second_col)


def is_nearest(first_square, second_square):
    first_row, first_col = notation_to_indexes(first_square)
    second_row, second_col = notation_to_indexes(second_square)
    return max([abs(first_row - second_row), abs(first_col - second_col)]) == 1

