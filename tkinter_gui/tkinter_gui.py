from tkinter import Event

from game import Game
from tkinter_gui.game_state import GameState
from tkinter_gui.main_window import MainWindow
from tkinter_gui.selected_piece import SelectedPiece


class TkInterGUI:

    def __init__(self, game: Game):
        self._game = game
        self._selected_piece = SelectedPiece()
        self._game_state = GameState(game, self._selected_piece)

        self._window = MainWindow(self._game_state)

        self.__bind_event_with_data("<<Square-Clicked>>", self.square_clicked)

    def square_clicked(self, event: Event):
        clicked_square = event.data["clicked_square"]
        if not self._selected_piece.is_set():
            piece = self._game.board[clicked_square]
            if piece is not None and piece.colour == self._game.current_player:
                self._selected_piece.set(self._game.board[clicked_square])
        else:
            self._game.make_move(self._selected_piece.position, clicked_square)
            self._selected_piece.reset()
        self.update()

    def update(self):
        self._window.update()

    def run(self):
        self.update()
        self._window.mainloop()

    def __bind_event_with_data(self, sequence, func, add=None):
        """
        Hack for handling data event arguments (not supported in TkInter)
        source: https://stackoverflow.com/a/23195921

        :param sequence:
        :param func:
        :param add:
        :return:
        """
        def substitute(*args):
            e = lambda: None
            e.data = eval(args[0])
            e.widget = self._window
            return e,

        funcid = self._window._register(func, substitute, needcleanup=1)
        cmd = """{0}if {{"[{1} %d]" == "break"}} break\n"""\
            .format('+' if add else '', funcid)
        self._window.tk.call("bind", self._window._w, sequence, cmd)

