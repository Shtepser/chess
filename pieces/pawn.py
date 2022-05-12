from colour import Colour
from pieces.piece import Piece


class Pawn(Piece):

    def can_move(self, to_position):
        if to_position[0] != self.file:
            return False
        to_rank = int(to_position[1])
        if to_rank == self.rank - 1 and 0 <= to_rank <= 7\
                and self._colour == Colour.BLACK:
            return True
        if to_rank == self.rank + 1 and 0 <= to_rank <= 7\
                and self._colour == Colour.WHITE:
            return True
        return False

    @property
    def symbol(self):
        return '♙' if self.colour == Colour.WHITE else '♟'

