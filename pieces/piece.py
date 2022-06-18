from abc import ABC, abstractmethod
from itertools import chain

from colour import Colour
from typing import Iterable

from utils import all_possible_squares


class Piece(ABC):

    def __init__(self, colour: Colour, board):
        """
        Initializes the piece of the given colour

        :param colour: the colour of the piece
        :param board: the board that the piece was placed at
        """
        self._colour = colour
        self._board = board
        self._already_moved = False

    def make_move(self, to_square: str) -> bool:
        """
        Makes an attempt to move the piece from its current position to another

        :param to_square: the position to try to move the piece to
        :return: True if the attempt was successful, False otherwise
        """
        if not self._can_move(to_square):
            return False
        self._board.move_piece(self.position, to_square)
        self._already_moved = True
        return True

    def possible_moves(self) -> Iterable[str]:
        """
        :return: All the squares the piece can be moved to
        """
        return chain(self.possible_ordinary_moves(), self.possible_takes())

    def possible_ordinary_moves(self) -> Iterable[str]:
        """
        :return: All the squares the piece can be moved to ordinary
                 (without taking an enemy piece)
        """
        return filter(self._can_move_ordinary, all_possible_squares())

    def possible_takes(self) -> Iterable[str]:
        """
        :return: All the squares on which the piece can currently take an enemy piece
        """
        return filter(self._can_take, all_possible_squares())

    def squares_under_attack(self) -> Iterable[str]:
        """
        :return: All the squares that are attacked by the piece
        """
        return filter(self._can_move, all_possible_squares())

    def attacks_square(self, square: str) -> bool:
        """
        :return: is the given square being attacked by the piece or not
        """
        return self._can_move(square)

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

    def _can_move_ordinary(self, to_square: str) -> bool:
        """
        Checks if the piece can be moved to the given square
        without taking enemy pieces

        :param to_square: the square that is checked
        :return: can piece be moved without taking an enemy piece or not
        """
        return self._board[to_square] is None and self._can_move(to_square)

    def _can_take(self, at_square: str) -> bool:
        """
        Checks if the piece can take an enemy piece at the given square

        :param at_square: the checked square
        :return: can piece take an enemy piece at the given square or not
        """
        return self._board[at_square] is not None \
            and self._board[at_square].colour != self.colour \
            and self._can_move(at_square)

    @property
    def colour(self) -> Colour:
        return self._colour

    @property
    def position(self) -> str:
        """
        :return: the square the piece is currently located at
        """
        return self._board.piece_position(self)

    @property
    def rank(self) -> int:
        return int(self.position[1])

    @property
    def file(self) -> str:
        return self.position[0]

    @property
    def already_moved(self) -> bool:
        """
        :return: has the piece moved during the current game or not
        """
        return self._already_moved

    @property
    @abstractmethod
    def symbol(self) -> str:
        """
        :return: UTF-8 character for the piece
        """
        pass

