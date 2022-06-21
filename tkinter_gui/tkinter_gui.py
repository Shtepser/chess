from tkinter import Tk, Canvas
from tkinter.constants import W, N, E, S
from tkinter.ttk import Frame, Label, Button

from game import Game


class TkInterGUI:

    def __init__(self, game: Game):
        self._game = game
        self._root = Tk()
        self._root.title("Chess")
        self._root.columnconfigure(0, weight=1)
        self._root.rowconfigure(0, weight=1)
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

        central_frame = Frame(screen, padding=(5, 5, 5, 5))
        central_frame.grid(column=0, row=1)
        self._board = Canvas(central_frame)
        self._board.grid(column=0, row=0)
        self._board.bind("<Button-1>", lambda x: self._draw_board())
        self._board.configure(width=500, height=500)

        footer = Frame(screen)
        footer.grid(column=0, row=2)
        footer.columnconfigure(0, weight=1)
        footer.columnconfigure(1, weight=1)
        footer.rowconfigure(0, weight=1)
        draw = Button(footer, text="Offer Draw")
        draw.grid(column=0, row=0)
        resign = Button(footer, text="Resign")
        resign.grid(column=1, row=0)

        self._root.minsize(800, 600)
        self._root.maxsize(800, 600)

    def _draw_board(self):
        self._board.delete("all")
        SIZE = 8
        LINE_COEFF = 0.05
        OFFSET = 10
        COORDINATES_WIDTH = 25
        BOARD_OFFSET = OFFSET + COORDINATES_WIDTH
        width, height = self._board.winfo_width(), self._board.winfo_height()
        side_length = min(width, height) - BOARD_OFFSET
        square_side = int(side_length / (SIZE + SIZE * LINE_COEFF))
        line_thickness = int(square_side * LINE_COEFF)
        print(side_length, square_side, line_thickness)
        side_length = square_side * SIZE
        for i in range(SIZE + 1):
            self._board.create_line(BOARD_OFFSET - line_thickness // 2, i * square_side + BOARD_OFFSET,
                                    side_length + BOARD_OFFSET + line_thickness // 2, i * square_side + BOARD_OFFSET,
                                    width=line_thickness)

            self._board.create_line(i * square_side + BOARD_OFFSET, BOARD_OFFSET - line_thickness // 2,
                                    i * square_side + BOARD_OFFSET, side_length + BOARD_OFFSET + line_thickness // 2,
                                    width=line_thickness)
            file = chr(ord('A') + i)
            rank = str(i + 1)
            if i != SIZE:
                self._board.create_text(OFFSET, BOARD_OFFSET + i * square_side + square_side // 2, text=rank, justify="center", anchor='center', font="14")
                self._board.create_text(width - OFFSET, BOARD_OFFSET + i * square_side + square_side // 2, text=rank, justify="center", anchor='center', font="14")
                self._board.create_text(BOARD_OFFSET + i * square_side + square_side // 2, OFFSET, text=file, justify="center", anchor='center', font="14")
                self._board.create_text(BOARD_OFFSET + i * square_side + square_side // 2, height - OFFSET, text=file, justify="center", anchor='center', font="14")
                for j in range(SIZE):
                    fill = "#ffa12e" if (i + j) % 2 == 0 else "#9e2d1e"
                    self._board.create_rectangle(BOARD_OFFSET + line_thickness // 2 + square_side * i,
                                                 BOARD_OFFSET + line_thickness // 2 + square_side * j,
                                                 BOARD_OFFSET - line_thickness // 2 + square_side * (i + 1),
                                                 BOARD_OFFSET - line_thickness // 2 + square_side * (j + 1),
                                                 fill=fill, outline="")
                    if j == 6:
                        self._board.create_text(BOARD_OFFSET + line_thickness // 2 + square_side * i + square_side // 2,
                                                BOARD_OFFSET + line_thickness // 2 + square_side * j + square_side // 2,
                                                text='♙',
                                                font=("Arial", 32),
                                                anchor="center")
                    if j == 1:
                        self._board.create_text(BOARD_OFFSET + line_thickness // 2 + square_side * i + square_side // 2,
                                                BOARD_OFFSET + line_thickness // 2 + square_side * j + square_side // 2,
                                                text='♟',
                                                font=("Arial", 32),
                                                anchor="center")


    def run(self):
        self._root.mainloop()

