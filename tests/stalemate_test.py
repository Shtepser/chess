from board import Board
from colour import Colour
from pieces import King, Queen


def test_easy_stalemate():
    board = Board()
    pieces = [(King, Colour.WHITE, "F7"), (Queen, Colour.WHITE, "G6"),
              (King, Colour.BLACK, "H8")]
    for type_, colour, position in pieces:
        board.add_piece(position, type_, colour)
    assert not board.is_stalemate(Colour.WHITE)
    assert board.is_stalemate(Colour.BLACK)
