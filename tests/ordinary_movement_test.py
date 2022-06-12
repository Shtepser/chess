from typing import Iterable, Tuple

import pytest

from board import Board
from colour import Colour
from pieces import Rook, Pawn, Bishop, King, Knight, Queen


@pytest.mark.parametrize("position,another_pieces,possible_moves", [
    ("A1",
     [],
     {"B2", "C3", "D4", "E5", "F6", "G7", "H8"}),
    ("A1",
     [(Rook, Colour.WHITE, "D4")],
     {"B2", "C3"}),
    ("E4",
     [(Pawn, Colour.WHITE, "C2")],
     {"D3", "F3", "G2", "H1", "D5", "C6", "B7", "A8", "F5", "G6", "H7"}),
    ("E4",
     [(Pawn, Colour.WHITE, "C2"), (Rook, Colour.WHITE, "B7")],
     {"D3", "F3", "G2", "H1", "D5", "C6", "F5", "G6", "H7"}),
])
def test_bishop_movement(position: str,
                         another_pieces: Iterable[Tuple[type, Colour, str]],
                         possible_moves: Iterable[str]):
    _assert_possible_moves_equals(Bishop, position, another_pieces, possible_moves)


@pytest.mark.parametrize("position,another_pieces,possible_moves", [
    ("A1",
     [],
     {"A2", "B1", "B2"}),
    ("E6",
     [],
     {"E5", "E7", "D5", "D6", "D7", "F5", "F6", "F7"}),
    ("E1",
     [(Queen, Colour.WHITE, "D1")],
     {"D2", "E2", "F2", "F1"})
])
def test_king_movement(position: str,
                       another_pieces: Iterable[Tuple[type, Colour, str]],
                       possible_moves: Iterable[str]):
    _assert_possible_moves_equals(King, position, another_pieces, possible_moves)


@pytest.mark.parametrize("position,another_pieces,possible_moves", [
    ("A1",
     [],
     {"C2", "B3"}),
    ("F8",
     [],
     {"D7", "E6", "G6", "H7"}),
    ("D5",
     [],
     {"C7", "E7", "F6", "F4", "E3", "C3", "B4", "B6"}),
    ("D5",
     [(Pawn, Colour.WHITE, "C4"), (Pawn, Colour.WHITE, "D4"),
      (Pawn, Colour.WHITE, "C5"), (Pawn, Colour.WHITE, "C6"),
      (Pawn, Colour.WHITE, "D6"), (Pawn, Colour.WHITE, "E6"),
      (Pawn, Colour.WHITE, "E5"), (Pawn, Colour.WHITE, "E4")],
     {"C7", "E7", "F6", "F4", "E3", "C3", "B4", "B6"}),
])
def test_knight_movement(position: str,
                         another_pieces: Iterable[Tuple[type, Colour, str]],
                         possible_moves: Iterable[str]):
    _assert_possible_moves_equals(Knight, position, another_pieces, possible_moves)


@pytest.mark.parametrize("position,colour,already_moved,"
                         "another_pieces,possible_moves", [
                             ("E2", Colour.WHITE, False,
                              [],
                              {"E3", "E4"}),
                             ("E3", Colour.WHITE, True,
                              [],
                              {"E4"}),
                             ("E3", Colour.WHITE, True,
                              [(Pawn, Colour.BLACK, "E4"),
                               (Pawn, Colour.BLACK, "F4")],
                              {}),
                             ("E2", Colour.WHITE, False,
                              [(Pawn, Colour.BLACK, "E3")],
                              {}),
                             ("C7", Colour.BLACK, False,
                              [],
                              {"C6", "C5"})
                         ])
def test_pawn_movement(position: str, colour: Colour, already_moved: bool,
                       another_pieces: Iterable[Tuple[type, Colour, str]],
                       possible_moves: Iterable[str]):
    board = Board()
    board.add_piece(position, Pawn, colour)
    for type_, colour, pos in another_pieces:
        board.add_piece(pos, type_, colour)
    pawn = board[position]
    if already_moved:
        pawn._already_moved = True
    assert set(pawn.possible_ordinary_moves()) == set(possible_moves)


@pytest.mark.parametrize("position,another_pieces,possible_moves", [
    ("A1",
     [],
     {"A2", "A3", "A4", "A5", "A6", "A7", "A8",
      "B1", "C1", "D1", "E1", "F1", "G1", "H1",
      "B2", "C3", "D4", "E5", "F6", "G7", "H8"}),
    ("E4",
     [(Pawn, Colour.WHITE, "E3"), (Rook, Colour.WHITE, "C4"),
      (Pawn, Colour.WHITE, "C2")],
     {"E5", "E6", "E7", "E8", "F4", "G4", "H4", "D4",
      "D3", "F5", "G6", "H7", "F3", "G2", "H1",
      "D5", "C6", "B7", "A8"})
])
def test_queen_movement(position: str,
                        another_pieces: Iterable[Tuple[type, Colour, str]],
                        possible_moves: Iterable[str]):
    _assert_possible_moves_equals(Queen, position, another_pieces, possible_moves)


@pytest.mark.parametrize("position,another_pieces,possible_moves", [
    ("A1",
     [],
     {"A2", "A3", "A4", "A5", "A6", "A7", "A8",
      "B1", "C1", "D1", "E1", "F1", "G1", "H1"}),
    ("A1",
     [(Rook, Colour.WHITE, "F1")],
     {"A2", "A3", "A4", "A5", "A6", "A7", "A8",
      "B1", "C1", "D1", "E1"}),
    ("E4",
     [(Pawn, Colour.WHITE, "E3"), (Rook, Colour.WHITE, "C4")],
     {"E5", "E6", "E7", "E8", "F4", "G4", "H4", "D4"})
])
def test_rook_movement(position: str,
                       another_pieces: Iterable[Tuple[type, Colour, str]],
                       possible_moves: Iterable[str]):
    _assert_possible_moves_equals(Rook, position, another_pieces, possible_moves)


def _assert_possible_moves_equals(piece_type, position: str,
                                  another_pieces, possible_moves):
    board = Board()
    board.add_piece(position, piece_type, Colour.WHITE)
    for type_, colour, pos in another_pieces:
        board.add_piece(pos, type_, colour)
    piece = board[position]
    assert set(piece.possible_ordinary_moves()) == set(possible_moves)
