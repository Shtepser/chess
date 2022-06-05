def notation_to_indexes(notation: str):
    if len(notation) != 2:
        raise ValueError(f"{notation} is not a valid cell position"
                          " in chess notation")
    col, row = notation
    col = ord(col) - ord('A')
    row = int(row) - 1
    if not (0 <= row <= 7 and 0 <= col <= 7):
        raise ValueError(f"{notation} is not a valid cell position"
                          " in chess notation")
    return row, col


def indexes_to_notation(row: int, col: int):
    return f"{col_to_file(col)}{row + 1}"


def col_to_file(col: int):
    return chr(ord('A') + col)


def on_same_file(first_cell, second_cell):
    return first_cell[0] == second_cell[0]


def on_same_rank(first_cell, second_cell):
    return int(first_cell[1]) == int(second_cell[1])


def on_same_diagonal(first_cell, second_cell):
    first_row, first_col = notation_to_indexes(first_cell)
    second_row, second_col = notation_to_indexes(second_cell)
    return abs(first_row - second_row) == abs(first_col - second_col)


def is_nearest(first_cell, second_cell):
    first_row, first_col = notation_to_indexes(first_cell)
    second_row, second_col = notation_to_indexes(second_cell)
    return max([abs(first_row - second_row), abs(first_col - second_col)]) == 1

