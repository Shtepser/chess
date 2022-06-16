from typing import Iterable, Tuple

import pytest

from board import Board
from colour import Colour
from pieces import Rook, Pawn, Bishop, King, Knight, Queen


@pytest.mark.parametrize("position,another_pieces,possible_takes", [
    ("A1",
     [],
     {}),
    ("A1",
     [(Rook, Colour.BLACK, "D5")],
     {}),
    ("A1",
     [(Rook, Colour.WHITE, "D4")],
     {}),
    ("A1",
     [(Rook, Colour.BLACK, "D4")],
     {"D4"}),
    ("A1",
     [(Rook, Colour.BLACK, "D4"), (Rook, Colour.BLACK, "C3")],
     {"C3"}),
    ("A1",
     [(Rook, Colour.BLACK, "D4"), (Rook, Colour.WHITE, "C3")],
     {}),
    ("D4",
     [(Rook, Colour.BLACK, "F2"), (Rook, Colour.BLACK, "B6")],
     {"F2", "B6"}),
])
def test_bishop_possible_takes(position: str,
                               another_pieces: Iterable[Tuple[type, Colour, str]],
                               possible_takes: Iterable[str]):
    _assert_possible_takes_equals(Bishop, position, another_pieces, possible_takes)


@pytest.mark.parametrize("position,another_pieces,possible_takes", [
    ("E6",
     [(Rook, Colour.BLACK, "E5")],
     {"E5"}),
    ("E5",
     [(Rook, Colour.BLACK, "E6"), (Rook, Colour.BLACK, "D4")],
     {"E6", "D4"}),
])
def test_king_possible_takes(position: str,
                       another_pieces: Iterable[Tuple[type, Colour, str]],
                       possible_takes: Iterable[str]):
    _assert_possible_takes_equals(King, position, another_pieces, possible_takes)
 
 
@pytest.mark.parametrize("position,another_pieces,possible_takes", [
    ("C5",
     [],
     {}),
    ("C5",
     [(Pawn, Colour.WHITE, "D6"),
      (Pawn, Colour.WHITE, "D5"),
      (Pawn, Colour.WHITE, "D4"),
      (Pawn, Colour.BLACK, "E4"),
      (Pawn, Colour.BLACK, "E6"),
      (Pawn, Colour.BLACK, "D3"),
      (Pawn, Colour.BLACK, "B3"),
      (Pawn, Colour.BLACK, "A4"),
      (Pawn, Colour.BLACK, "A6"),
      (Pawn, Colour.BLACK, "B7"),
      (Pawn, Colour.BLACK, "D7"),
      (Pawn, Colour.BLACK, "A5")],
     {"E4", "E6", "D3", "B3", "A4", "A6", "B7", "D7"}),
])
def test_knight_possible_takes(position: str,
                         another_pieces: Iterable[Tuple[type, Colour, str]],
                         possible_takes: Iterable[str]):
    _assert_possible_takes_equals(Knight, position, another_pieces, possible_takes)


# @pytest.mark.parametrize("position,colour,already_moved,"
#                          "another_pieces,possible_moves", [
#                              ("E2", Colour.WHITE, False,
#                               [],
#                               {"E3", "E4"}),
#                              ("E3", Colour.WHITE, True,
#                               [],
#                               {"E4"}),
#                              ("E3", Colour.WHITE, True,
#                               [(Pawn, Colour.BLACK, "E4"),
#                                (Pawn, Colour.BLACK, "F4")],
#                               {}),
#                              ("E2", Colour.WHITE, False,
#                               [(Pawn, Colour.BLACK, "E3")],
#                               {}),
#                              ("C7", Colour.BLACK, False,
#                               [],
#                               {"C6", "C5"})
#                          ])
# def test_pawn_possible_takes(position: str, colour: Colour, already_moved: bool,
#                        another_pieces: Iterable[Tuple[type, Colour, str]],
#                        possible_moves: Iterable[str]):
#     board = Board()
#     board.add_piece(position, Pawn, colour)
#     for type_, colour, pos in another_pieces:
#         board.add_piece(pos, type_, colour)
#     pawn = board[position]
#     if already_moved:
#         pawn._already_moved = True
#     assert set(pawn.possible_ordinary_moves()) == set(possible_moves)
# 
# 
# @pytest.mark.parametrize("position,another_pieces,possible_moves", [
#     ("A1",
#      [],
#      {"A2", "A3", "A4", "A5", "A6", "A7", "A8",
#       "B1", "C1", "D1", "E1", "F1", "G1", "H1",
#       "B2", "C3", "D4", "E5", "F6", "G7", "H8"}),
#     ("E4",
#      [(Pawn, Colour.WHITE, "E3"), (Rook, Colour.WHITE, "C4"),
#       (Pawn, Colour.WHITE, "C2")],
#      {"E5", "E6", "E7", "E8", "F4", "G4", "H4", "D4",
#       "D3", "F5", "G6", "H7", "F3", "G2", "H1",
#       "D5", "C6", "B7", "A8"})
# ])
# def test_queen_possible_takes(position: str,
#                         another_pieces: Iterable[Tuple[type, Colour, str]],
#                         possible_moves: Iterable[str]):
#     _assert_possible_takes_equals(Queen, position, another_pieces, possible_moves)
# 
# 
# @pytest.mark.parametrize("position,another_pieces,possible_moves", [
#     ("A1",
#      [],
#      {"A2", "A3", "A4", "A5", "A6", "A7", "A8",
#       "B1", "C1", "D1", "E1", "F1", "G1", "H1"}),
#     ("A1",
#      [(Rook, Colour.WHITE, "F1")],
#      {"A2", "A3", "A4", "A5", "A6", "A7", "A8",
#       "B1", "C1", "D1", "E1"}),
#     ("E4",
#      [(Pawn, Colour.WHITE, "E3"), (Rook, Colour.WHITE, "C4")],
#      {"E5", "E6", "E7", "E8", "F4", "G4", "H4", "D4"})
# ])
# def test_rook_possible_takes(position: str,
#                        another_pieces: Iterable[Tuple[type, Colour, str]],
#                        possible_moves: Iterable[str]):
#     _assert_possible_takes_equals(Rook, position, another_pieces, possible_moves)
# 

def _assert_possible_takes_equals(piece_type, position: str,
                                  another_pieces, possible_takes):
    board = Board()
    board.add_piece(position, piece_type, Colour.WHITE)
    for type_, colour, pos in another_pieces:
        board.add_piece(pos, type_, colour)
    piece = board[position]
    assert set(piece.possible_takes()) == set(possible_takes)
