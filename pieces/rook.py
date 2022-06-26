from colour import Colour
from pieces.piece import Piece
from utils import on_same_file, on_same_rank


class Rook(Piece):

    def attacks_square(self, square: str) -> bool:
        return (on_same_file(self.position, square)
                or on_same_rank(self.position, square)) \
               and self._board.exists_free_route(self.position, square)

    @property
    def symbol(self):
        return '♖' if self.colour == Colour.WHITE else '♜'

