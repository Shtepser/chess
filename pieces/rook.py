from colour import Colour
from pieces.piece import Piece


class Rook(Piece):

    def can_move(self, to_position):
        if self.position == to_position:
            return False
        if self._board[to_position] is not None\
                and self._board[to_position].colour == self.colour:
            return False
        if self.position[0] == to_position[0] \
                or self.position[1] == to_position[1]:
            return self._board.exists_free_route(self.position,
                                                 to_position)
        return False

    @property
    def symbol(self):
        return '♖' if self.colour == Colour.WHITE else '♜'

