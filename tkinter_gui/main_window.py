from tkinter import Tk
from tkinter.ttk import Frame


class MainWindow(Tk):

    def __init__(self):
        super().__init__()
        self.title("Chess")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.minsize(800, 600)
        self.maxsize(800, 600)

        self.screen = Frame(self, padding=(10, 10, 10, 10))
        self.screen.grid(column=0, row=0)
        self.screen.columnconfigure(0, weight=1)
        self.screen.rowconfigure(0, weight=1)
        self.screen.rowconfigure(1, weight=1)
        self.screen.rowconfigure(2, weight=1)

