from colour import Colour
from pieces.piece import Piece
from utils import on_same_file


class Pawn(Piece):

    def _can_move(self, to_position):
        if not on_same_file(self.position,
                            to_position)\
                or not self._board.exists_free_route(self.position,
                                                     to_position):
            return False
        to_rank = int(to_position[1])
        possible_distance = 1 if self.already_moved else 2
        if self._colour == Colour.WHITE:
            return 1 <= (to_rank - self.rank) <= possible_distance \
                    and 0 <= to_rank <= 7
        return 1 <= (self.rank - to_rank) <= possible_distance \
                and 0 <= to_rank <= 7\

    @property
    def symbol(self):
        return '♙' if self.colour == Colour.WHITE else '♟'

