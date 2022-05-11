from colour import Colour
from pieces.piece import Piece


class Pawn(Piece):

    def can_move(self, to_row, to_col):
        if to_col != self.col:
            return False
        if to_row == self.row - 1 and 0 <= to_row <= 7\
                and self._colour == Colour.BLACK:
            return True
        if to_row == self.row + 1 and 0 <= to_row <= 7\
                and self._colour == Colour.WHITE:
            return True
        return False

    @property
    def symbol(self):
        return '♙' if self.colour == Colour.WHITE else '♟'

