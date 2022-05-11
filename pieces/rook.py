from colour import Colour
from pieces.piece import Piece


class Rook(Piece):

    def can_move(self, to_row, to_col):
        if self.coords == (to_row, to_col):
            return False
        if self._board.cell(to_row, to_col) is not None\
                and self._board.cell(to_row, to_col).colour == self.colour:
            return False
        if self.row == to_row or self.col == to_col:
            return self._board.exists_free_route(self.row, self.col, to_row, to_col)
        return False

    @property
    def symbol(self):
        return '♖' if self.colour == Colour.WHITE else '♜'

