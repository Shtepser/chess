from colour import Colour
from pieces.piece import Piece
from utils import on_same_diagonal, on_same_file, on_same_rank


class Queen(Piece):

    def attacks_square(self, square: str) -> bool:
        return any(map(lambda x: x(self.position, square),
                       [on_same_file, on_same_rank, on_same_diagonal])) \
                and self._board.exists_free_route(self.position, square)

    @property
    def symbol(self):
        return '♕' if self.colour == Colour.WHITE else '♛'

