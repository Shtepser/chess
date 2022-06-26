from colour import Colour
from pieces.piece import Piece
from utils import is_nearest


class King(Piece):

    def attacks_square(self, square) -> bool:
        return is_nearest(self.position, square)

    @property
    def symbol(self):
        return '♔' if self.colour == Colour.WHITE else '♚'

