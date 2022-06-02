from colour import Colour
from pieces.piece import Piece
from utils import on_same_diagonal, on_same_file, on_same_rank


class Queen(Piece):

    def _can_move(self, to_position):
        return self._can_move_ordinary(to_position)\
                or self._can_castle(to_position)

    def _can_move_ordinary(self, to_position):
        return any(map(lambda x: x(self.position, to_position),
                       [on_same_file, on_same_rank, on_same_diagonal])) \
                and self._board.exists_free_route(self.position,
                                                 to_position)
    def _can_castle(self, to_position):
        False

    @property
    def symbol(self):
        return '♕' if self.colour == Colour.WHITE else '♛'

