from board import Board
from colour import Colour
from pieces import Pawn, Rook, Knight, Bishop, Queen, King


class Game:

    def __init__(self):
        self._board = Board()
        self._current_player = Colour.WHITE
        self._initial_placement()

    def switch_player(self):
        self._current_player = Colour.WHITE \
            if self._current_player == Colour.BLACK \
            else Colour.BLACK

    def _initial_placement(self):
        for col_ix in range(8):
            self._board.add_piece(1, col_ix, Pawn, Colour.WHITE)
            self._board.add_piece(6, col_ix, Pawn, Colour.BLACK)
        self._board.add_piece(0, 0, Rook, Colour.WHITE)
        self._board.add_piece(0, 7, Rook, Colour.WHITE)
        self._board.add_piece(7, 0, Rook, Colour.BLACK)
        self._board.add_piece(7, 7, Rook, Colour.BLACK)
        self._board.add_piece(0, 1, Knight, Colour.WHITE)
        self._board.add_piece(0, 6, Knight, Colour.WHITE)
        self._board.add_piece(7, 1, Knight, Colour.BLACK)
        self._board.add_piece(7, 6, Knight, Colour.BLACK)
        self._board.add_piece(0, 2, Bishop, Colour.WHITE)
        self._board.add_piece(0, 5, Bishop, Colour.WHITE)
        self._board.add_piece(7, 2, Bishop, Colour.BLACK)
        self._board.add_piece(7, 5, Bishop, Colour.BLACK)
        self._board.add_piece(0, 3, Queen, Colour.WHITE)
        self._board.add_piece(7, 3, Queen, Colour.BLACK)
        self._board.add_piece(0, 4, King, Colour.WHITE)
        self._board.add_piece(7, 4, King, Colour.BLACK)

    @property
    def current_player(self):
        return self._current_player

