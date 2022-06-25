import ast
from tkinter import Tk, Event
from tkinter.constants import W, N, E, S
from tkinter.ttk import Frame, Label, Button

from game import Game
from tkinter_gui.board_view import BoardView


class TkInterGUI:

    def __init__(self, game: Game):
        self._game = game
        self._root = Tk()
        self._root.title("Chess")
        self._root.columnconfigure(0, weight=1)
        self._root.rowconfigure(0, weight=1)

        self._root.minsize(800, 600)
        self._root.maxsize(800, 600)

        screen = Frame(self._root, padding=(10, 10, 10, 10))
        screen.grid(column=0, row=0, sticky=(N, W, E, S))
        screen.columnconfigure(0, weight=1)
        screen.rowconfigure(0, weight=1)
        screen.rowconfigure(1, weight=1)
        screen.rowconfigure(2, weight=1)

        header = Frame(screen)
        header.columnconfigure(0, weight=1)
        header.rowconfigure(0, weight=1)
        header.rowconfigure(1, weight=1)
        header.grid(column=0, row=0)
        player = Label(header, text="Current turn: white")
        player.grid(column=0, row=0)
        status = Label(header, text="Make your turn!")
        status.grid(column=0, row=1)

        central_frame = BoardView(self._game.board, screen)
        central_frame.grid(column=0, row=1)

        footer = Frame(screen)
        footer.grid(column=0, row=2)
        footer.columnconfigure(0, weight=1)
        footer.columnconfigure(1, weight=1)
        footer.rowconfigure(0, weight=1)
        draw = Button(footer, text="Offer Draw")
        draw.grid(column=0, row=0)
        resign = Button(footer, text="Resign")
        resign.grid(column=1, row=0)

        self.__bind_event_with_data("<<Square-Clicked>>", self.square_clicked)

    def square_clicked(self, event: Event):
        print(event.data)

    def run(self):
        self._root.mainloop()

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
            e.widget = self._root
            return e,

        funcid = self._root._register(func, substitute, needcleanup=1)
        cmd = """{0}if {{"[{1} %d]" == "break"}} break\n"""\
            .format('+' if add else '', funcid)
        self._root.tk.call("bind", self._root._w, sequence, cmd)

