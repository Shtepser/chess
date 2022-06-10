from colour import Colour
from pieces.piece import Piece
from utils import notation_to_indexes, on_same_file


class Pawn(Piece):

    def _can_move(self, to_position):
        return self.can_attack(to_position) \
                or self._can_move_ordinary(to_position)

    def can_attack(self, position: str) -> bool:
        return self._is_attacked_cell(position) \
                and self._board[position] is not None \
                and self._board[position].colour != self.colour

    def _can_move_ordinary(self, position):
        if not on_same_file(self.position, position) \
                or not self._board.exists_free_route(self.position, position):
            return False
        if self._board[position] is not None:
            return False
        to_rank = int(position[1])
        possible_distance = 1 if self.already_moved else 2
        if self.colour == Colour.WHITE:
            return 1 <= (to_rank - self.rank) <= possible_distance \
                    and 0 <= to_rank <= 7
        return 1 <= (self.rank - to_rank) <= possible_distance \
                and 0 <= to_rank <= 7

    def _is_attacked_cell(self, position):
        self_rank, self_file = notation_to_indexes(self.position)
        rank, file = notation_to_indexes(position)
        if abs(file - self_file) != 1:
            return False
        if self._colour == Colour.WHITE:
            return rank - self_rank == 1
        return rank - self_rank == -1

    @property
    def symbol(self):
        return '♙' if self.colour == Colour.WHITE else '♟'
