from game import Game
from tkinter_gui.selected_piece import SelectedPiece


class GameState:

    def __init__(self, game: Game, selected_piece: SelectedPiece):
        self._game = game
        self._selected_piece = selected_piece

    @property
    def current_player(self):
        return self._game.current_player.name.lower()

    @property
    def current_player_is_in_check(self):
        return self._game.current_player_is_in_check()

    @property
    def board(self):
        return self._game.board

    @property
    def selected_piece(self):
        return self._selected_piece

