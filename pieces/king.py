from colour import Colour
from utils import notation_to_indexes
from pieces.piece import Piece


class King(Piece):

    def can_move(self, to_position):
        if to_position == self.position:
            return False
        if self._board[to_position] is not None\
                and self._board[to_position].colour == self.colour:
            return False
        from_row, from_col = notation_to_indexes(self.position)
        to_row, to_col = notation_to_indexes(to_position)
        return max([abs(from_row - to_row), abs(from_col - to_col)]) == 1

    @property
    def symbol(self):
        return '♔' if self.colour == Colour.WHITE else '♚'

