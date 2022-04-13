from colour import Colour
from pieces.piece import Piece


class King(Piece):

    def can_move(self, to_row, to_col):
        if (to_row, to_col) == self.coords:
            return False
        if self._board[to_row][to_col] is not None\
                and self._board[to_row][to_col].colour == self.colour:
            return False
        return max([abs(self.row - to_row), abs(self.col - to_col)]) == 1

    @property
    def symbol(self):
        return '♔' if self.colour == Colour.WHITE else '♚'

