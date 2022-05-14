from colour import Colour
from pieces.piece import Piece
from utils import on_same_file


class Pawn(Piece):

    def _can_move(self, to_position):
        if not on_same_file(self.position, to_position):
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

