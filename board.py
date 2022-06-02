from utils import notation_to_indexes, indexes_to_notation


_SIZE = 8


class Board:

    def __init__(self):
        self._cells = [None for _ in range(_SIZE ** 2)]

    def add_piece(self, row, col, piece_type, colour):
        self._cells[row * _SIZE + col] = piece_type(colour, self)

    def move_piece(self, from_, to):
        row_from, col_from = notation_to_indexes(from_)
        row_to, col_to = notation_to_indexes(to)
        piece = self._cells[row_from * _SIZE + col_from]
        self._cells[row_from * _SIZE + col_from] = None
        self._cells[row_to * _SIZE + col_to] = piece

    def cell(self, row, col):
        return self._cells[row * _SIZE + col]

    def piece_position(self, piece):
        for ix, cell in enumerate(self._cells):
            if cell == piece:
                row, col = ix // 8, ix % 8
                return indexes_to_notation(row, col)

    def exists_free_route(self, from_, to):
        row_from, col_from = notation_to_indexes(from_)
        row_to, col_to = notation_to_indexes(to)
        if row_from == row_to:
            return self._exists_free_horizontal_route(row_from, col_from,
                                                      col_to)
        if col_from == col_to:
            return self._exists_free_vertical_route(row_from, row_to,
                                                    col_from)
        if abs(row_from - row_to) == abs(col_from - col_to):
            return self._exists_free_diagonal_route(row_from, col_from,
                                                    row_to, col_to)
        return False

    def is_under_attack(self, position, colour):
        return any(map(lambda x: x.can_attack(position),
                       self._all_pieces(colour)))

    def _all_pieces(self, colour=None):
        pieces = filter(lambda x: x is not None, self._cells)
        if colour is not None:
            pieces = filter(lambda x: x.colour == colour, pieces)
        return pieces

    def _exists_free_horizontal_route(self, row, col_from, col_to):
        first_col, last_col = sorted([col_from, col_to])
        for col in range(first_col + 1, last_col):
            if self.cell(row, col) is not None:
                return False
        return True

    def _exists_free_vertical_route(self, row_from, row_to, col):
        first_row, last_row = sorted([row_from, row_to])
        for row in range(first_row + 1, last_row):
            if self.cell(row, col) is not None:
                return False
        return True

    def _exists_free_diagonal_route(self, row_from, col_from, row_to, col_to):
        col_step = 1 if col_from < col_to else -1
        row_step = 1 if row_from < row_to else -1
        for step in range(1, abs(row_from - row_to)):
            row_ix = row_from + row_step * step
            col_ix = col_from + col_step * step
            if self.cell(row_ix, col_ix) is not None:
                return False
        return True

    def __getitem__(self, key: str):
        row, col = notation_to_indexes(key)
        return self._cells[row * _SIZE + col]

    def __setitem__(self, key: str, value):
        row, col = notation_to_indexes(key)
        self._cells[row * _SIZE + col] = value

