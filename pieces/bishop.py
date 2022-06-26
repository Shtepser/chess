from colour import Colour
from pieces.piece import Piece
from utils import on_same_diagonal


class Bishop(Piece):

    def attacks_square(self, square):
        return on_same_diagonal(self.position, square) \
                and self._board.exists_free_route(self.position, square)

    @property
    def symbol(self):
        return '♗' if self.colour == Colour.WHITE else '♝'

