from board import Board
from colour import Colour
from pieces import Pawn, Rook, Knight, Bishop, Queen, King
from utils import col_to_file


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
            file = col_to_file(col_ix)
            self._board.add_piece(f"{file}2", Pawn, Colour.WHITE)
            self._board.add_piece(f"{file}7", Pawn, Colour.BLACK)
        self._board.add_piece("A1", Rook, Colour.WHITE)
        self._board.add_piece("H1", Rook, Colour.WHITE)
        self._board.add_piece("A8", Rook, Colour.BLACK)
        self._board.add_piece("H8", Rook, Colour.BLACK)
        self._board.add_piece("B1", Knight, Colour.WHITE)
        self._board.add_piece("G1", Knight, Colour.WHITE)
        self._board.add_piece("B8", Knight, Colour.BLACK)
        self._board.add_piece("G8", Knight, Colour.BLACK)
        self._board.add_piece("C1", Bishop, Colour.WHITE)
        self._board.add_piece("F1", Bishop, Colour.WHITE)
        self._board.add_piece("C8", Bishop, Colour.BLACK)
        self._board.add_piece("F8", Bishop, Colour.BLACK)
        self._board.add_piece("D1", Queen, Colour.WHITE)
        self._board.add_piece("D8", Queen, Colour.BLACK)
        self._board.add_piece("E1", King, Colour.WHITE)
        self._board.add_piece("E8", King, Colour.BLACK)

    def current_player_is_in_check(self):
        return self._board.is_king_in_check(self.current_player)

    @property
    def current_player(self):
        return self._current_player

