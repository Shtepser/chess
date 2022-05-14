from colour import Colour
from pieces.piece import Piece
from utils import on_same_file, on_same_rank


class Rook(Piece):

    def _can_move(self, to_position):
        return (on_same_file(self.position, to_position) \
                or on_same_rank(self.position, to_position)) \
               and self._board.exists_free_route(self.position, to_position)

    @property
    def symbol(self):
        return '♖' if self.colour == Colour.WHITE else '♜'

