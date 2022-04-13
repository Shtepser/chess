from colour import Colour
from piece import Piece


class Pawn(Piece):

    def can_move(self, to_row, to_col):
        if to_col != self.col:
            return False
        if to_row == self.row - 1 and 0 <= to_row <= 7\
                and self._colour == Colour.BLACK:

            return True
        if to_row == self.row + 1 and 0 <= to_row <= 7\
                and self._colour == Colour.WHITE:
            self._board[self.row][self.col] = None
            self._board[to_row][to_col] = self
            return True
        return False

    @property
    def symbol(self):
        return '♙' if self.colour == Colour.BLACK else '♟'

