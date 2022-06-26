from board import Board
from colour import Colour
from pieces import Pawn, Rook, King, Queen, Bishop, Knight


def test_everlasting_game_final():
    board = Board()
    pieces = [(Rook, Colour.WHITE, "D1"), (King, Colour.WHITE, "G1"),
              (Pawn, Colour.WHITE, "A2"), (Pawn, Colour.WHITE, "F2"),
              (Pawn, Colour.WHITE, "G2"), (Pawn, Colour.WHITE, "H2"),
              (Pawn, Colour.WHITE, "C3"), (Queen, Colour.BLACK, "F3"),
              (Bishop, Colour.BLACK, "B6"), (Pawn, Colour.WHITE, "F6"),
              (Pawn, Colour.BLACK, "A7"), (Bishop, Colour.BLACK, "B7"),
              (Pawn, Colour.BLACK, "C7"), (Bishop, Colour.WHITE, "D7"),
              (Bishop, Colour.WHITE, "E7"), (Pawn, Colour.BLACK, "F7"),
              (Pawn, Colour.WHITE, "H7"), (Rook, Colour.BLACK, "B8"),
              (King, Colour.BLACK, "F8"), (Rook, Colour.BLACK, "G8")]
    for type_, colour, position in pieces:
        board.add_piece(position, type_, colour)
    assert not board.is_checkmate(Colour.WHITE)
    assert board.is_checkmate(Colour.BLACK)


def test_everlasting_game_pre_final():
    board = Board()
    pieces = [(Rook, Colour.WHITE, "D1"), (King, Colour.WHITE, "G1"),
              (Pawn, Colour.WHITE, "A2"), (Pawn, Colour.WHITE, "F2"),
              (Pawn, Colour.WHITE, "G2"), (Pawn, Colour.WHITE, "H2"),
              (Bishop, Colour.BLACK, "A3"),
              (Pawn, Colour.WHITE, "C3"), (Queen, Colour.BLACK, "F3"),
              (Bishop, Colour.BLACK, "B6"), (Pawn, Colour.WHITE, "F6"),
              (Pawn, Colour.BLACK, "A7"), (Bishop, Colour.BLACK, "B7"),
              (Pawn, Colour.BLACK, "C7"), (Bishop, Colour.WHITE, "D7"),
              (Knight, Colour.BLACK, "E7"), (Pawn, Colour.BLACK, "F7"),
              (Pawn, Colour.WHITE, "H7"), (Rook, Colour.BLACK, "B8"),
              (King, Colour.BLACK, "F8"), (Rook, Colour.BLACK, "G8")]
    for type_, colour, position in pieces:
        board.add_piece(position, type_, colour)
    assert not board.is_checkmate(Colour.WHITE)
    assert not board.is_checkmate(Colour.BLACK)


def test_immortal_game_final():
    board = Board()
    pieces = [(Queen, Colour.BLACK, "A1"), (Pawn, Colour.WHITE, "A2"),
              (Knight, Colour.BLACK, "A6"), (Pawn, Colour.BLACK, "A7"),
              (Rook, Colour.BLACK, "A8"), (Pawn, Colour.BLACK, "B5"),
              (Pawn, Colour.WHITE, "C2"), (Bishop, Colour.BLACK, "C8"),
              (Pawn, Colour.WHITE, "D3"), (Knight, Colour.WHITE, "D5"),
              (Pawn, Colour.BLACK, "D7"), (King, Colour.BLACK, "D8"),
              (King, Colour.WHITE, "E2"), (Pawn, Colour.WHITE, "E5"),
              (Bishop, Colour.WHITE, "E7"), (Knight, Colour.BLACK, "F6"),
              (Pawn, Colour.BLACK, "F7"), (Bishop, Colour.BLACK, "G1"),
              (Pawn, Colour.WHITE, "G4"), (Knight, Colour.WHITE, "G7"),
              (Pawn, Colour.WHITE, "H5"), (Pawn, Colour.BLACK, "H7"),
              (Rook, Colour.BLACK, "H8")]
    for type_, colour, position in pieces:
        board.add_piece(position, type_, colour)
    assert not board.is_checkmate(Colour.WHITE)
    assert board.is_checkmate(Colour.BLACK)


def test_stalemate_is_not_checkmate():
    board = Board()
    pieces = [(King, Colour.WHITE, "F7"), (Queen, Colour.WHITE, "G6"),
              (King, Colour.BLACK, "H8")]
    for type_, colour, position in pieces:
        board.add_piece(position, type_, colour)
    assert not board.is_checkmate(Colour.WHITE)
    assert not board.is_checkmate(Colour.BLACK)

