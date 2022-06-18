from utils import indexes_to_notation


class ConsoleUI:

    def __init__(self, game):
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
                position_of_piece_to_move = input("Position of the piece you want to move: ")
                try:
                    piece_to_move = self._game._board[position_of_piece_to_move]
                except ValueError as e:
                    print(f"Incorrect input: {str(e)}")
                    continue
                if piece_to_move is None:
                    print(f"No piece at square {position_of_piece_to_move}")
                    continue
                if piece_to_move.colour != self._game.current_player:
                    print("You can't move an enemy piece!")
                    continue
                position_to_move = input("Position of the square you want to move the piece to: ")
                try:
                    success = piece_to_move.make_move(position_to_move)
                    if not success:
                        print(f"Can't move piece from {position_of_piece_to_move} to " +\
                              f"{position_to_move}")
                        continue
                except ValueError as e:
                    print(f"Incorrect input: {str(e)}")
                    continue
                moved = True
            self._game.switch_player()

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

