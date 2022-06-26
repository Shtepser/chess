from typing import Iterable, Tuple

import pytest

from board import Board
from colour import Colour
from pieces import Rook, Pawn, Bishop, King, Knight, Queen


@pytest.mark.parametrize("position,another_pieces,possible_takes", [
    ("A1",
     [(King, Colour.WHITE, "A8"), (King, Colour.BLACK, "A6")],
     {}),
    ("A1",
     [(Rook, Colour.BLACK, "D5"),
      (King, Colour.WHITE, "A8"), (King, Colour.BLACK, "A6")],
     {}),
    ("A1",
     [(Rook, Colour.WHITE, "D4"),
      (King, Colour.WHITE, "A8"), (King, Colour.BLACK, "A6")],
     {}),
    ("A1",
     [(Rook, Colour.BLACK, "D4"),
      (King, Colour.WHITE, "A8"), (King, Colour.BLACK, "A6")],
     {"D4"}),
    ("A1",
     [(Rook, Colour.BLACK, "D4"), (Rook, Colour.BLACK, "C3"),
      (King, Colour.WHITE, "A8"), (King, Colour.BLACK, "A6")],
     {"C3"}),
    ("A1",
     [(Rook, Colour.BLACK, "D4"), (Rook, Colour.WHITE, "C3"),
      (King, Colour.WHITE, "A8"), (King, Colour.BLACK, "A6")],
     {}),
    ("D4",
     [(Rook, Colour.BLACK, "F2"), (Rook, Colour.BLACK, "B6"),
      (King, Colour.WHITE, "C4"), (King, Colour.BLACK, "A4")],
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
     [(King, Colour.WHITE, "H6"), (King, Colour.BLACK, "H8")],
     {}),
    ("C5",
     [(Pawn, Colour.WHITE, "D6"), (Pawn, Colour.WHITE, "D5"),
      (Pawn, Colour.WHITE, "D4"), (Pawn, Colour.BLACK, "E4"),
      (Pawn, Colour.BLACK, "E6"), (Pawn, Colour.BLACK, "D3"),
      (Pawn, Colour.BLACK, "B3"), (Pawn, Colour.BLACK, "A4"),
      (Pawn, Colour.BLACK, "A6"), (Pawn, Colour.BLACK, "B7"),
      (Pawn, Colour.BLACK, "D7"), (Pawn, Colour.BLACK, "A5"),
      (King, Colour.WHITE, "H6"), (King, Colour.BLACK, "H8")],
     {"E4", "E6", "D3", "B3", "A4", "A6", "B7", "D7"}),
])
def test_knight_possible_takes(position: str,
                         another_pieces: Iterable[Tuple[type, Colour, str]],
                         possible_takes: Iterable[str]):
    _assert_possible_takes_equals(Knight, position, another_pieces, possible_takes)


@pytest.mark.parametrize("position,colour,another_pieces,possible_takes", [
                             ("E2", Colour.WHITE,
                              [(King, Colour.WHITE, "H6"),
                               (King, Colour.BLACK, "H8")],
                              {}),
                             ("F5", Colour.BLACK,
                              [(King, Colour.WHITE, "H6"),
                               (King, Colour.BLACK, "H8")],
                              {}),
                             ("E2", Colour.WHITE,
                              [(Pawn, Colour.BLACK, "E3"),
                               (King, Colour.WHITE, "H6"),
                               (King, Colour.BLACK, "H8")],
                              {}),
                             ("E2", Colour.WHITE,
                              [(Pawn, Colour.BLACK, "F4"),
                               (King, Colour.WHITE, "H6"),
                               (King, Colour.BLACK, "H8")],
                              {}),
                             ("E3", Colour.WHITE,
                              [(Pawn, Colour.BLACK, "F4"),
                               (King, Colour.WHITE, "H6"),
                               (King, Colour.BLACK, "H8")],
                              {"F4"}),
                             ("E7", Colour.BLACK,
                              [(Pawn, Colour.WHITE, "F6"),
                               (King, Colour.WHITE, "H6"),
                               (King, Colour.BLACK, "H8")],
                              {"F6"}),
                             ("E7", Colour.WHITE,
                              [(Pawn, Colour.BLACK, "F6")],
                              {}),
                             ("E3", Colour.WHITE,
                              [(Pawn, Colour.BLACK, "E4"),
                               (Pawn, Colour.BLACK, "F4"),
                               (King, Colour.WHITE, "H6"),
                               (King, Colour.BLACK, "H8")],
                              {"F4"}),
                             ("E3", Colour.WHITE,
                              [(Pawn, Colour.BLACK, "F4"),
                               (Pawn, Colour.BLACK, "D4"),
                               (King, Colour.WHITE, "H6"),
                               (King, Colour.BLACK, "H8")],
                              {"F4", "D4"}),
                             ("E3", Colour.WHITE,
                              [(Pawn, Colour.BLACK, "E4"),
                               (Pawn, Colour.BLACK, "F4"),
                               (Pawn, Colour.BLACK, "D4"),
                               (King, Colour.WHITE, "H6"),
                               (King, Colour.BLACK, "H8")],
                              {"F4", "D4"}),
                         ])
def test_pawn_possible_takes(position: str, colour: Colour,
                       another_pieces: Iterable[Tuple[type, Colour, str]],
                       possible_takes: Iterable[str]):
    board = Board()
    board.add_piece(position, Pawn, colour)
    for piece_type, piece_colour, pos in another_pieces:
        board.add_piece(pos, piece_type, piece_colour)
    pawn = board[position]
    assert set(pawn.possible_takes()) == set(possible_takes)


@pytest.mark.parametrize("position,another_pieces,possible_takes", [
    ("A1",
     [(King, Colour.WHITE, "B8"), (King, Colour.BLACK, "B6")],
     {}),
    ("E4",
     [(Pawn, Colour.BLACK, "E3"), (Rook, Colour.BLACK, "C4"),
      (Pawn, Colour.WHITE, "C2"),
      (King, Colour.BLACK, "C5"), (King, Colour.WHITE, "C8")],
     {"C4", "E3"}),
    ("E4",
     [(Pawn, Colour.WHITE, "E3"), (Rook, Colour.WHITE, "C4"),
      (Pawn, Colour.BLACK, "C2"),
      (King, Colour.WHITE, "C6"), (King, Colour.BLACK, "C8")],
     {"C2"})
])
def test_queen_possible_takes(position: str,
                        another_pieces: Iterable[Tuple[type, Colour, str]],
                        possible_takes: Iterable[str]):
    _assert_possible_takes_equals(Queen, position, another_pieces, possible_takes)


@pytest.mark.parametrize("position,another_pieces,possible_takes", [
    ("E4",
     [(King, Colour.WHITE, "C6"), (King, Colour.BLACK, "C8")],
     {}),
    ("E4",
     [(Rook, Colour.BLACK, "H4"),
      (King, Colour.WHITE, "C6"), (King, Colour.BLACK, "C8")],
     {"H4"}),
    ("E4",
     [(Rook, Colour.BLACK, "H4"), (Rook, Colour.WHITE, "G4"),
      (King, Colour.WHITE, "C6"), (King, Colour.BLACK, "C8")],
     {}),
    ("E4",
     [(Rook, Colour.BLACK, "E8"),
      (King, Colour.WHITE, "C6"), (King, Colour.BLACK, "C8")],
     {"E8"}),
    ("E4",
     [(Rook, Colour.BLACK, "D2"), (Rook, Colour.BLACK, "G7"),
      (Rook, Colour.BLACK, "G6"),
      (King, Colour.WHITE, "C6"), (King, Colour.BLACK, "C8")],
     {}),
])
def test_rook_possible_takes(position: str,
                       another_pieces: Iterable[Tuple[type, Colour, str]],
                       possible_takes: Iterable[str]):
    _assert_possible_takes_equals(Rook, position, another_pieces, possible_takes)


def _assert_possible_takes_equals(piece_type, position: str,
                                  another_pieces, possible_takes):
    board = Board()
    board.add_piece(position, piece_type, Colour.WHITE)
    for type_, colour, pos in another_pieces:
        board.add_piece(pos, type_, colour)
    piece = board[position]
    assert set(piece.possible_takes()) == set(possible_takes)

