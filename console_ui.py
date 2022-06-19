from game import Game
from utils import indexes_to_notation


class ConsoleUI:

    def __init__(self, game: Game):
        self._game = game
        print("The game has started\n\n")

    def run(self):
        while True:
            print()
            self._show_board()
            print()
            print(f"Current move: {self._game.current_player.name.capitalize()}")
            if self._game.current_player_is_in_check():
                print("KING IN CHECK!")
            moved = False
            while not moved:
                square_from = input("Position of the piece you want to move: ")
                square_to = input("Position of the square you want to move the piece to: ")
                result = self._game.make_move(square_from, square_to) 
                match result:
                    case Game.MoveResult.NO_SUCH_SQUARE_FROM | \
                            Game.MoveResult.NO_SUCH_SQUARE_TO:
                        print(f"Incorrect input: {square_from}:{square_to}!")
                    case Game.MoveResult.NO_PIECE_AT_SQUARE:
                        print(f"No piece at square {square_from}!")
                    case Game.MoveResult.PIECE_IS_ENEMY:
                        print("You can't move an enemy piece!")
                    case Game.MoveResult.INCORRECT_MOVE:
                        print(f"Can't move piece from {square_from} to " +\
                              f"{square_to}")
                    case _:
                        moved = True

    def _show_board(self):
        print("  ", '-' * 17, sep='')
        for row_ix in range(7, -1, -1):
            row = [self._game._board[indexes_to_notation(row_ix, col_ix)]
                   for col_ix in range(8)]
            print(f"{row_ix + 1} |", '|'.join(map(self._square_to_char, row)), '|',
                  sep='')
            print("  ", '-' * 17, sep='')
        print("   ", " ".join(map(lambda x: chr(ord('A') + x), range(8))), sep='')
    
    @staticmethod
    def _square_to_char(square):
        return square.symbol if square is not None else ' '

