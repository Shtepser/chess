from colour import Colour
from piece import Piece


class Rook(Piece):

    def can_move(self, to_row, to_col):
        if self.coords == (to_row, to_col):
            return False
        if self._board[to_row][to_col] is not None\
                and self._board[to_row][to_col].colour == self.colour:
            return False
        if self.row == to_row:
            first_col, last_col = sorted([self.col, to_col])
            for col in range(first_col + 1, last_col):
                if self._board[to_row][col] is not None:
                    return False
            return True
        if self.col== to_col:
            first_row, last_row = sorted([self.row, to_row])
            for row in range(first_row + 1, last_row):
                if self._board[row][to_col] is not None:
                    return False
            return True
        return False

    @property
    def symbol(self):
        return '♜' if self.colour == Colour.WHITE else '♖'

