from tkinter import Variable
from tkinter.ttk import Frame, Label

from tkinter_gui.game_state import GameState


class StatusFrame(Frame):

    def __init__(self, game_state: GameState, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._game_state = game_state
        self._current_player = Variable()
        self._status = Variable()

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        current_player_label = Label(self, textvariable=self._current_player)
        current_player_label.grid(column=0, row=0)

        status_label = Label(self, textvariable=self._status)
        status_label.grid(column=0, row=1)

    def update(self):
        super().update()
        self._current_player.set(f"Current move: {self._game_state.current_player}")
        self._status.set("Make your move!"
                         if not self._game_state.current_player_is_in_check
                         else "Your king in check!")

