from typing import Iterable, Tuple

import pytest

from board import Board
from colour import Colour
from pieces import Rook, Pawn, Bishop, King, Queen, Knight


@pytest.mark.parametrize("pieces,is_white_king_in_check", [
    ([(King, Colour.WHITE, "F1"), (King, Colour.BLACK, "E8"),
      (Pawn, Colour.WHITE, "A2"), (Pawn, Colour.WHITE, "C2"),
      (Bishop, Colour.BLACK, "G1"), (Queen, Colour.BLACK, "A1")],
     True),
    ([(King, Colour.WHITE, "F1"), (King, Colour.BLACK, "E8"),
      (Pawn, Colour.WHITE, "A2"), (Pawn, Colour.WHITE, "C2"),
      (Rook, Colour.WHITE, "A1"),
      (Bishop, Colour.BLACK, "G1"), (Queen, Colour.BLACK, "B2")],
     False),
    ([(King, Colour.WHITE, "F2"), (King, Colour.BLACK, "E8"),
      (Pawn, Colour.WHITE, "A2"), (Pawn, Colour.WHITE, "C2"),
      (Bishop, Colour.BLACK, "G1"), (Queen, Colour.BLACK, "A1")],
     True),
    ([(King, Colour.WHITE, "E2"), (King, Colour.BLACK, "E8"),
      (Pawn, Colour.WHITE, "A2"), (Pawn, Colour.WHITE, "C2"),
      (Bishop, Colour.BLACK, "G1"), (Queen, Colour.BLACK, "A1")],
     False),
    ([(King, Colour.WHITE, "E1"), (King, Colour.BLACK, "E8"),
      (Knight, Colour.WHITE, "D1"),
      (Knight, Colour.BLACK, "D3"), (Queen, Colour.BLACK, "A1")],
     True)
])
def test_king_in_check(pieces: Iterable[Tuple[type, Colour, str]],
                       is_white_king_in_check: bool):
    board = Board()
    for type_, colour, pos in pieces:
        board.add_piece(pos, type_, colour)
    assert board.is_king_in_check(Colour.WHITE) == is_white_king_in_check

