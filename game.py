from colour import Colour
from rook import Rook
from pawn import Pawn


class Game:

    def __init__(self):
        self._board = [[None for _ in range(8)] for _ in range(8)]
        self._current_player = Colour.WHITE
        self._initial_placement()

    def switch_player(self):
        self._current_player = Colour.WHITE \
            if self._current_player == Colour.BLACK \
            else Colour.BLACK

    def _initial_placement(self):
        for row in self._board:
            for col_ix in range(len(row)):
                row[col_ix] = None
        for col_ix in range(8):
            self._board[1][col_ix] = Pawn(Colour.WHITE, self._board)
            self._board[6][col_ix] = Pawn(Colour.BLACK, self._board)
        self._board[0][0] = Rook(Colour.WHITE, self._board)
        self._board[0][7] = Rook(Colour.WHITE, self._board)
        self._board[7][0] = Rook(Colour.BLACK, self._board)
        self._board[7][7] = Rook(Colour.BLACK, self._board)



    @property
    def current_player(self):
        return self._current_player

