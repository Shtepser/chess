from abc import ABC, abstractmethod

from colour import Colour


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

    @abstractmethod
    def can_move(self, to_position: str) -> bool:
        pass

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

