from colour import Colour
from piece import Piece


class Bishop(Piece):

    def can_move(self, to_row, to_col):
        if (to_row, to_col) == self.coords:
            return False
        if self._board[to_row][to_col] is not None\
                and self._board[to_row][to_col].colour == self.colour:
            return False
        if abs(self.row - to_row) != abs(self.col - to_col):
            return False
        col_step = 1 if self.col < to_col else -1
        row_step = 1 if self.row < to_row else -1
        for col_ix in range(self.col + col_step, to_col, col_step):
            for row_ix in range(self.row + row_step, to_row, row_step):
                if self._board[row_ix][col_ix] is not None:
                    return False
        return True

    @property
    def symbol(self):
        return '♗' if self.colour == Colour.WHITE else '♝'

