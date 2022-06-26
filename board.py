from typing import Iterable

from colour import Colour
from pieces import King
from pieces.piece import Piece
from utils import notation_to_indexes, indexes_to_notation

_SIZE = 8


class Board:

    def __init__(self):
        self._squares = [None for _ in range(_SIZE ** 2)]

    def add_piece(self, position, piece_type, colour):
        row, col = notation_to_indexes(position)
        self._squares[row * _SIZE + col] = piece_type(colour, self)

    def move_piece(self, from_, to):
        row_from, col_from = notation_to_indexes(from_)
        row_to, col_to = notation_to_indexes(to)
        piece = self._squares[row_from * _SIZE + col_from]
        self._squares[row_from * _SIZE + col_from] = None
        self._squares[row_to * _SIZE + col_to] = piece

    def is_king_in_check(self, colour: Colour) -> bool:
        """
        Check if the king of the given colour is in check

        :param colour: the colour of the king that is checked for check
        :return: is the king of the given colour is in check or not
        """
        try:
            king = next(filter(lambda x: isinstance(x, King),
                               self._all_pieces(colour)))
        except StopIteration:
            raise RuntimeError(f"The {colour.name.lower()} king is missing!")
        opposite_colour = Colour.BLACK if colour is Colour.WHITE \
            else Colour.WHITE
        return self._is_under_attack(king.position, opposite_colour)

    def is_checkmate(self, colour: Colour) -> bool:
        return self.is_king_in_check(colour) and \
            all(map(lambda x: len(list(x.possible_moves())) == 0,
                    self._all_pieces(colour)))

    def is_stalemate(self, current_move_colour: Colour) -> bool:
        return all(map(lambda x: len(list(x.possible_moves())) == 0,
                       self._all_pieces(current_move_colour)))

    def square(self, row, col):
        return self._squares[row * _SIZE + col]

    def piece_position(self, piece):
        for ix, square in enumerate(self._squares):
            if square == piece:
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

    def _is_under_attack(self, square: str, colour: Colour) -> bool:
        """
        Check if the square is being attacked by
        any of the pieces of the given colour

        :param square: the square checked for being under attack
        :param colour: the colour of the pieces that are checked
                       to attack the square
        """
        return any(map(lambda x: x.attacks_square(square),
                       self._all_pieces(colour)))

    def _all_pieces(self, colour=None) -> Iterable[Piece]:
        pieces = filter(lambda x: x is not None, self._squares)
        if colour is not None:
            pieces = filter(lambda x: x.colour == colour, pieces)
        return pieces

    def _exists_free_horizontal_route(self, row, col_from, col_to):
        first_col, last_col = sorted([col_from, col_to])
        for col in range(first_col + 1, last_col):
            if self.square(row, col) is not None:
                return False
        return True

    def _exists_free_vertical_route(self, row_from, row_to, col):
        first_row, last_row = sorted([row_from, row_to])
        for row in range(first_row + 1, last_row):
            if self.square(row, col) is not None:
                return False
        return True

    def _exists_free_diagonal_route(self, row_from, col_from, row_to, col_to):
        col_step = 1 if col_from < col_to else -1
        row_step = 1 if row_from < row_to else -1
        for step in range(1, abs(row_from - row_to)):
            row_ix = row_from + row_step * step
            col_ix = col_from + col_step * step
            if self.square(row_ix, col_ix) is not None:
                return False
        return True

    def __getitem__(self, key: str):
        row, col = notation_to_indexes(key)
        return self.square(row, col)

    def __setitem__(self, key: str, value):
        row, col = notation_to_indexes(key)
        self._squares[row * _SIZE + col] = value

    def __deepcopy__(self, memodict={}):
        copy_ = Board()
        for piece in self._all_pieces():
            copy_.add_piece(piece.position, type(piece), piece.colour)
        return copy_

