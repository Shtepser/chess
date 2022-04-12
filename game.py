from colour import Colour
from rook import Rook
from pawn import Pawn


class Game:

    def __init__(self):
        self._board = [[None for _ in range(8)] for _ in range(8)]
        self._board[4][4] = Pawn(Colour.WHITE, self._board)
        self._board[1][4] = Rook(Colour.BLACK, self._board)
        self._current_player = Colour.WHITE

    def next_player(self):
        self._current_player = Colour.WHITE \
            if self._current_player == Colour.BLACK \
            else Colour.WHITE

    def run(self):
        # TODO implement me!
        def _show_board():
            print('-' * 17)
            for row in self._board:
                print('|', '|'.join(map(Game.cell_to_char, row)), '|',
                      sep='')
                print('-' * 17)

        _show_board()
        self._board[4][4].make_move(5, 4)
        _show_board()
        for row in range(8):
            for col in range(8):
                print(str(self._board[1][4].can_move(row, col)).ljust(5), end=' ')
            print()

    @staticmethod
    def cell_to_char(cell):
        return cell.symbol if cell is not None else ' '

