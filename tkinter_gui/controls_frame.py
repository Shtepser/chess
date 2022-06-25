from tkinter.ttk import Frame, Button

from tkinter_gui.game_state import GameState


class ControlsFrame(Frame):

    def __init__(self, game_state: GameState, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._game_state = game_state
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        draw = Button(self, text="Offer Draw")
        draw.grid(column=0, row=0)
        resign = Button(self, text="Resign")
        resign.grid(column=1, row=0)

    def update(self):
        super().update()

