from colour import Colour
from utils import notation_to_indexes
from pieces.piece import Piece


class Knight(Piece):

    def can_move(self, to_position):
        if to_position == self.position:
            return False
        if self._board[to_position] is not None\
                and self._board[to_position].colour == self.colour:
            return False
        from_row, from_col = notation_to_indexes(self.position)
        to_row, to_col = notation_to_indexes(to_position)
        return (abs(to_row - from_row), abs(to_col - from_col))\
                in {(1, 2), (2, 1)}

    @property
    def symbol(self):
        return '♘' if self.colour == Colour.WHITE else '♞'

