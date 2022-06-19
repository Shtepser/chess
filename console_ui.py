from game import Game
from utils import indexes_to_notation


class ConsoleUI:

    def __init__(self, game: Game):
        self._game = game
        self._running = False
        self._last_attempt = None
        self._last_result = None
        print("The game has started\n\n")

    def run(self):
        self._running = True
        while self._running:
            self._game_loop()

    def _game_loop(self):
        self._draw()
        self._move_piece()

    def _draw(self):
        print()
        self._draw_board()
        print()
        self._draw_state()

    def _move_piece(self):
        self._last_result = None
        while self._last_result != Game.MoveResult.SUCCESS:
            self._last_attempt = self._prompt_move()
            self._last_result = self._game.make_move(*self._last_attempt)
            self._report_move_result()

    def _report_move_result(self):
        square_from, square_to = self._last_attempt
        match self._last_result:
            case Game.MoveResult.NO_SUCH_SQUARE_FROM | \
                    Game.MoveResult.NO_SUCH_SQUARE_TO:
                print(f"Incorrect input: {square_from}:{square_to}!")
            case Game.MoveResult.NO_PIECE_AT_SQUARE:
                print(f"No piece at square {square_from}!")
            case Game.MoveResult.PIECE_IS_ENEMY:
                print("You can't move an enemy piece!")
            case Game.MoveResult.INCORRECT_MOVE:
                print(f"Can't move piece from {square_from} to " +
                      f"{square_to}")
            case _:
                pass

    def _prompt_move(self):
        square_from = input("Position of the piece you want to move: ")
        square_to = input("Position of the square you want "
                          "to move the piece to: ")
        return square_from, square_to

    def _draw_state(self):
        print(f"Current move: {self._game.current_player.name.capitalize()}")
        if self._game.current_player_is_in_check():
            print("KING IN CHECK!")

    def _draw_board(self):
        print("  ", '-' * 17, sep='')
        for row_ix in range(7, -1, -1):
            row = [self._game._board[indexes_to_notation(row_ix, col_ix)]
                   for col_ix in range(8)]
            print(f"{row_ix + 1} |", '|'.join(map(self._square_to_char,
                                                  row)), '|', sep='')
            print("  ", '-' * 17, sep='')
        print("   ", " ".join(map(lambda x: chr(ord('A') + x), range(8))),
              sep='')

    @staticmethod
    def _square_to_char(square):
        return square.symbol if square is not None else ' '

