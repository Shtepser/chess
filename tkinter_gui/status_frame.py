from tkinter import Variable
from tkinter.ttk import Frame, Label

from game import Game
from tkinter_gui.game_state import GameState


class StatusFrame(Frame):

    def __init__(self, game_state: GameState, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._game_state = game_state
        self._current_player = Variable()
        self._status = Variable()
        self._last_move_result = Variable()

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        current_player_label = Label(self, textvariable=self._current_player, font=("Roman", 12))
        current_player_label.grid(column=0, row=0)

        status_label = Label(self, textvariable=self._status, font=("Roman", 12))
        status_label.grid(column=0, row=1)

        last_move_result_label = Label(self, textvariable=self._last_move_result,
                                       font=("Roman", 12))
        last_move_result_label.grid(column=0, row=2)

    def update(self):
        super().update()
        self._current_player.set(f"Current move: {self._game_state.current_player}")
        self._status.set("Make your move!"
                         if not self._game_state.current_player_is_in_check
                         else "Your king in check!")
        self._last_move_result.set({
            Game.MoveResult.SUCCESS: "",
            Game.MoveResult.INCORRECT_MOVE: "Incorrect move!",
            Game.MoveResult.PIECE_IS_ENEMY: "ERROR! Report a bug PIECE_IS_ENEMY",
            Game.MoveResult.NO_SUCH_SQUARE_TO: "ERROR! Report a bug NO_SUCH_SQUARE_TO",
            Game.MoveResult.NO_SUCH_SQUARE_FROM: "ERROR! Report a bug NO_SUCH_SQUARE_FROM",
            Game.MoveResult.NO_PIECE_AT_SQUARE: "ERROR! Report a bug NO_SUCH_PIECE_AT_SQUARE"
        }[self._game_state.last_move_status])

