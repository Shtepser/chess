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
            moved = False
            while not moved:
                piece_to_move = input("Row and column of the piece you want to move: ")
                if len(piece_to_move.split()) != 2\
                        or not all(map(str.isdigit, piece_to_move.split()))\
                        or not all(map(lambda x: 0 <= x <= 7,
                                       map(int, piece_to_move.split()))):
                    print("Incorrect input")
                    continue
                row_from, col_from = [int(i) for i in piece_to_move.split()]
                piece_to_move = self._game._board.cell(row_from, col_from)
                if piece_to_move is None:
                    print(f"No piece at cell {row_from},{col_from}")
                    continue
                if piece_to_move.colour != self._game.current_player:
                    print("You can't move an enemy piece!")
                    continue
                cell_to_move = input("Row and column of the cell you want to move the piece to: ")
                if len(cell_to_move.split()) != 2\
                        or not all(map(str.isdigit, cell_to_move.split()))\
                        or not all(map(lambda x: 0 <= x <= 7,
                                       map(int, cell_to_move.split()))):
                    print("Incorrect input")
                    continue
                row_to, col_to = [int(i) for i in cell_to_move.split()]
                cell_to_move = self._game._board.cell(row_to, col_to)
                if not piece_to_move.can_move(row_to, col_to):
                    print(f"Can't move piece from {row_from},{col_from} to " +\
                          f"{row_to},{col_to}")
                    continue
                piece_to_move.make_move(row_to, col_to)
                moved = True
            self._game.switch_player()

    def _show_board(self):
        print("  ", '-' * 17, sep='')
        for row_ix in range(7, -1, -1):
            row = self._game._board._cells[row_ix]
            print(f"{row_ix} |", '|'.join(map(self._cell_to_char, row)), '|',
                  sep='')
            print("  ", '-' * 17, sep='')
        print("   ", " ".join(map(str, range(8))), sep='')
    
    @staticmethod
    def _cell_to_char(cell):
        return cell.symbol if cell is not None else ' '

