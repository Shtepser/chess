from tkinter import Tk
from tkinter.ttk import Frame

from tkinter_gui.board_view import BoardView
from tkinter_gui.controls_frame import ControlsFrame
from tkinter_gui.game_state import GameState
from tkinter_gui.status_frame import StatusFrame


class MainWindow(Tk):

    def __init__(self, game_state: GameState):
        super().__init__()
        self.title("Chess")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.minsize(800, 600)
        self.maxsize(800, 600)

        self._screen = Frame(self, padding=(10, 10, 10, 10))
        self._screen.grid(column=0, row=0)
        self._screen.columnconfigure(0, weight=1)
        self._screen.rowconfigure(0, weight=1)
        self._screen.rowconfigure(1, weight=1)
        self._screen.rowconfigure(2, weight=1)

        self._header = StatusFrame(game_state, self._screen)
        self._header.grid(column=0, row=0)

        self._central_frame = BoardView(game_state, self._screen)
        self._central_frame.grid(column=0, row=1)

        self._footer = ControlsFrame(game_state, self._screen)
        self._footer.grid(column=0, row=2)

    def update(self):
        super().update()
        self._central_frame.update()
        self._header.update()
        self._footer.update()

