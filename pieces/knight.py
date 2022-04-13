from colour import Colour
from pieces.piece import Piece


class Knight(Piece):

    def can_move(self, to_row, to_col):
        if (to_row, to_col) == self.coords:
            return False
        if self._board[to_row][to_col] is not None\
                and self._board[to_row][to_col].colour == self.colour:
            return False
        return (abs(to_row - self.row), abs(to_col - self.col))\
                in {(1, 2), (2, 1)}

    @property
    def symbol(self):
        return '♘' if self.colour == Colour.WHITE else '♞'

