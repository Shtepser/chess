from colour import Colour
from pieces.piece import Piece
from utils import notation_to_indexes


class Knight(Piece):

    def attacks_square(self, square: str) -> bool:
        from_row, from_col = notation_to_indexes(self.position)
        to_row, to_col = notation_to_indexes(square)
        return (abs(to_row - from_row), abs(to_col - from_col))\
                in {(1, 2), (2, 1)}

    @property
    def symbol(self):
        return '♘' if self.colour == Colour.WHITE else '♞'

