from colour import Colour
from pieces.piece import Piece
from utils import notation_to_indexes, on_same_file


class Pawn(Piece):

    def _can_move(self, to_square):
        return self._can_take(to_square) or self._can_move_ordinary(to_square)

    def _can_take(self, at_square: str) -> bool:
        return self.attacks_square(at_square) \
               and self._board[at_square] is not None \
               and self._board[at_square].colour != self.colour \
               and self._is_move_on_general_rules(at_square)

    def _can_move_ordinary(self, to_square):
        if not self._is_move_on_general_rules(to_square):
            return False
        if not on_same_file(self.position, to_square) \
                or not self._board.exists_free_route(self.position, to_square):
            return False
        if self._board[to_square] is not None:
            return False
        to_rank = int(to_square[1])
        possible_distance = 1 if self.already_moved else 2
        if self.colour == Colour.WHITE:
            return 1 <= (to_rank - self.rank) <= possible_distance \
                   and 0 <= to_rank <= 7
        return 1 <= (self.rank - to_rank) <= possible_distance \
               and 0 <= to_rank <= 7

    def attacks_square(self, square):
        """
        Is the square one of the possibly attacked by the pawn

        :param square: the square to check
        :return:
        """
        self_row, self_col = notation_to_indexes(self.position)
        row, col = notation_to_indexes(square)
        if abs(col - self_col) != 1:
            return False
        if self._colour == Colour.WHITE:
            return row - self_row == 1
        return row - self_row == -1

    @property
    def symbol(self):
        return '♙' if self.colour == Colour.WHITE else '♟'

