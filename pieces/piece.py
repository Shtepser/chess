from abc import ABC, abstractmethod
from itertools import chain

from colour import Colour
from typing import Iterable


class Piece(ABC):

    def __init__(self, colour: Colour, board):
        self._colour = colour
        self._board = board
        self._already_moved = False

    def make_move(self, to_position: str):
        if not self.can_move(to_position):
            return False
        self._board.move_piece(self.position, to_position)
        self._already_moved = True
        return True

    def can_move(self, to_position: str) -> bool:
        if to_position == self.position:
            return False
        if self._board[to_position] is not None\
                and self._board[to_position].colour == self.colour:
            return False
        return self._can_move(to_position)

    @abstractmethod
    def _can_move(self, to_position: str) -> bool:
        pass

    def can_attack(self, position: str) -> bool:
        return self._board[position] is not None \
               and self._board[position].colour != self.colour \
               and self.can_move(position)

    def possible_ordinary_moves(self) -> Iterable[str]:
        return {f"{file}{rank}"
                for rank in range(1, 9) for file in 'ABCDEFGH'
                if self.can_move(f"{file}{rank}")
                and not self.can_attack(f"{file}{rank}")}

    def possible_attacks(self) -> Iterable[str]:
        return {f"{file}{rank}"
                for rank in range(1, 9) for file in 'ABCDEFGH'
                if self.can_attack(f"{file}{rank}")}

    def possible_moves(self) -> Iterable[str]:
        return chain(self.possible_ordinary_moves(), self.possible_attacks())

    @property
    def colour(self):
        return self._colour

    @property
    def position(self):
        return self._board.piece_position(self)

    @property
    def rank(self):
        return int(self.position[1])

    @property
    def file(self):
        return self.position[0]

    @property
    def already_moved(self):
        return self._already_moved

    @property
    @abstractmethod
    def symbol(self):
        pass
