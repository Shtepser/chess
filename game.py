from colour import Colour
from rook import Rook
from pawn import Pawn


class Game:

    def __init__(self):
        self._board = [[None for _ in range(8)] for _ in range(8)]
        self._board[4][4] = Pawn(Colour.WHITE, self._board)
        self._board[1][4] = Rook(Colour.BLACK, self._board)
        self._current_player = Colour.WHITE

    def switch_player(self):
        self._current_player = Colour.WHITE \
            if self._current_player == Colour.BLACK \
            else Colour.BLACK

    @property
    def current_player(self):
        return self._current_player

