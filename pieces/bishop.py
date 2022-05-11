from colour import Colour
from pieces.piece import Piece


class Bishop(Piece):

    def can_move(self, to_row, to_col):
        if (to_row, to_col) == self.coords:
            return False
        if self._board.cell(to_row, to_col) is not None\
                and self._board.cell(to_row, to_col).colour == self.colour:
            return False
        if abs(self.row - to_row) != abs(self.col - to_col):
            return False
        return self._board.exists_free_route(self.row, self.col, to_row, to_col)

    @property
    def symbol(self):
        return '♗' if self.colour == Colour.WHITE else '♝'

