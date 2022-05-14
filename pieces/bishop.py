from colour import Colour
from pieces.piece import Piece
from utils import on_same_diagonal


class Bishop(Piece):

    def _can_move(self, to_position):
        return on_same_diagonal(self.position, to_position) \
                and self._board.exists_free_route(self.position, to_position)

    @property
    def symbol(self):
        return '♗' if self.colour == Colour.WHITE else '♝'

