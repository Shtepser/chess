from tkinter import Event
from tkinter.ttk import Frame

from game import Game
from tkinter_gui.controls_frame import ControlsFrame
from tkinter_gui.game_state import GameState
from tkinter_gui.main_window import MainWindow
from tkinter_gui.selected_piece import SelectedPiece
from tkinter_gui.board_view import BoardView
from tkinter_gui.status_frame import StatusFrame


class TkInterGUI:

    def __init__(self, game: Game):
        self._game = game
        self._game_state = GameState(game)
        self._window = MainWindow()

        self._selected_piece = SelectedPiece()

        self._header = StatusFrame(self._game_state, self._window.screen)
        self._header.grid(column=0, row=0)

        self._central_frame = BoardView(self._game.board, self._selected_piece,
                                        self._window.screen)
        self._central_frame.grid(column=0, row=1)

        self._footer = ControlsFrame(self._game_state, self._window.screen)
        self._footer.grid(column=0, row=2)

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
        self._central_frame.update()
        self._header.update()
        self._footer.update()

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

