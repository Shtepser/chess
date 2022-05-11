from abc import ABC, abstractmethod

from colour import Colour


class Piece(ABC):

    def __init__(self, colour: Colour, board):
        self._colour = colour
        self._board = board
        self._already_moved = False

    def make_move(self, to_row: int, to_col: int):
        if not self.can_move(to_row, to_col):
            return False
        self._board[self.row][self.col] = None
        self._board[to_row][to_col] = self
        self._already_moved = True
        return True

    @abstractmethod
    def can_move(self, to_row: int, to_col: int) -> bool:
        pass

    @property
    def colour(self):
        return self._colour

    @property
    def coords(self):
        for row_ix, row in enumerate(self._board):
            for col_ix, cell in enumerate(row):
                if cell == self:
                    return row_ix, col_ix
    
    @property
    def row(self):
        return self.coords[0]

    @property
    def col(self):
        return self.coords[1]

    @property
    def already_moved(self):
        return self._already_moved

    @property
    @abstractmethod
    def symbol(self):
        pass

