from colour import Colour
from pieces.piece import Piece
from utils import is_nearest


class King(Piece):

    def _can_move(self, to_square):
        if not super()._can_move(to_square):
            return False
        return is_nearest(self.position, to_square)

    @property
    def symbol(self):
        return '♔' if self.colour == Colour.WHITE else '♚'

