from abc import ABC, abstractmethod
from itertools import chain

from colour import Colour
from typing import Iterable


class Piece(ABC):

    def __init__(self, colour: Colour, board):
        self._colour = colour
        self._board = board
        self._already_moved = False

    def make_move(self, to_position: str) -> bool:
        """
        Makes an attempt to move the piece from its current position to another

        :param to_position: the position to try to move the piece to
        :return: True if the attempt was successful, False otherwise
        """
        if not self._can_move(to_position):
            return False
        self._board.move_piece(self.position, to_position)
        self._already_moved = True
        return True

    def possible_moves(self) -> Iterable[str]:
        """
        :return: All the squares the piece can be moved to
        """
        return chain(self.possible_ordinary_moves(), self.squares_under_attack())

    def possible_ordinary_moves(self) -> Iterable[str]:
        """
        :return: All the squares the piece can be moved to ordinary
                 (without taking an enemy piece)
        """
        return {f"{file}{rank}"
                for rank in range(1, 9) for file in 'ABCDEFGH'
                if self._can_move(f"{file}{rank}")
                and not self.attacks_square(f"{file}{rank}")}

    def squares_under_attack(self) -> Iterable[str]:
        """
        :return: All the squares on which the piece can take an enemy piece
        """
        return {f"{file}{rank}"
                for rank in range(1, 9) for file in 'ABCDEFGH'
                if self.attacks_square(f"{file}{rank}")}

    @abstractmethod
    def _can_move(self, to_square: str) -> bool:
        """
        Checks if the piece can be moved from its current position to another

        :param to_square: position the possibility to move to is checked
        :return: can the piece be moved or not
        """
        if to_square == self.position:
            return False
        if self._board[to_square] is not None\
                and self._board[to_square].colour == self.colour:
            return False
        return True

    def attacks_square(self, square: str) -> bool:
        return self._board[square] is not None \
               and self._board[square].colour != self.colour \
               and self._can_move(square)

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

