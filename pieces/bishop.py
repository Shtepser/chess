from colour import Colour
from pieces.piece import Piece
from utils import on_same_diagonal


class Bishop(Piece):

    def _can_move(self, to_square):
        if not super()._can_move(to_square):
            return False
        return on_same_diagonal(self.position, to_square) \
                and self._board.exists_free_route(self.position, to_square)

    @property
    def symbol(self):
        return '♗' if self.colour == Colour.WHITE else '♝'

