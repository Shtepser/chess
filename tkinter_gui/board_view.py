from __future__ import annotations
from tkinter import Frame, Canvas

from board import Board
from utils import indexes_to_notation


class BoardView(Frame):
    SIZE = 8

    class BoardViewParams:

        _LINE_WIDTH_COEFFICIENT = 0.05
        _OFFSET = 10
        _COORDINATES_WIDTH = 25
        _BOARD_OFFSET = _OFFSET + _COORDINATES_WIDTH
        _WHITE_SQUARES_COLOUR = "#ffa12e"
        _BLACK_SQUARES_COLOUR = "#9e2d1e"
        _MARKS_FONT = "Roman"
        _MARKS_FONT_SIZE = 14
        _PIECES_FONT = "Arial"
        _PIECES_FONT_SIZE = 40

        def __init__(self, canvas_to_draw: Canvas, size: int):
            width, height = canvas_to_draw.winfo_width(), \
                            canvas_to_draw.winfo_height()
            side_length = min(width, height) - self._BOARD_OFFSET * 2
            self.square_side = int(side_length / size)
            self.line_width = int(self.square_side * self._LINE_WIDTH_COEFFICIENT)
            self.side_length = self.square_side * size

        @property
        def board_offset(self):
            return self._BOARD_OFFSET

        @property
        def white_colour(self):
            return self._WHITE_SQUARES_COLOUR

        @property
        def black_colour(self):
            return self._BLACK_SQUARES_COLOUR

        @property
        def marks_params(self):
            return {"justify": "center", "anchor": "center",
                    "font": (self._MARKS_FONT, str(self._MARKS_FONT_SIZE))}

        @property
        def pieces_params(self):
            return {"anchor": "center",
                    "font": (self._PIECES_FONT, str(self._PIECES_FONT_SIZE))}

    def __init__(self, board: Board, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._board = board
        self._canvas = Canvas(self)
        self._canvas.grid(column=0, row=0)
        self._canvas.bind("<Button-1>", lambda x: self._redraw())
        self._canvas.configure(width=500, height=500)
        self.update_params()

    def _redraw(self):
        self.update_params()
        self._clear_canvas()
        self._draw_grid()
        self._draw_marks()
        self._fill_squares()
        self._draw_pieces()

    def update_params(self):
        self.params = BoardView.BoardViewParams(self._canvas, self.SIZE)

    def _clear_canvas(self):
        self._canvas.delete("all")

    def _draw_grid(self):
        x_start = y_start = self.params.board_offset - self.params.line_width // 2
        x_end = y_end = self.params.side_length \
                        + self.params.board_offset \
                        + self.params.line_width // 2,
        for i in range(self.SIZE + 1):
            line_offset = i * self.params.square_side + self.params.board_offset
            self._canvas.create_line(x_start, line_offset, x_end, line_offset,
                                     width=self.params.line_width)
            self._canvas.create_line(line_offset, y_start, line_offset, y_end,
                                     width=self.params.line_width)

    def _draw_marks(self):
        self._draw_rank_marks()
        self._draw_file_marks()

    def _draw_rank_marks(self):
        left_column_left_offset = self.params.board_offset // 2
        right_column_left_offset = self.params.board_offset + self.params.side_length\
                                   + self.params.board_offset // 2
        for i in range(self.SIZE):
            rank = str(self.SIZE - i)
            top_offset = self.params.board_offset + i * self.params.square_side + \
                         self.params.square_side // 2
            self._canvas.create_text(left_column_left_offset, top_offset, text=rank,
                                     **self.params.marks_params)
            self._canvas.create_text(right_column_left_offset, top_offset, text=rank,
                                     **self.params.marks_params)

    def _draw_file_marks(self):
        top_row_top_offset = self.params.board_offset // 2
        lower_row_top_offset = self.params.board_offset + self.params.side_length \
                             + self.params.board_offset // 2,
        for i in range(self.SIZE):
            file = chr(ord('A') + i)
            left_offset = self.params.board_offset + i * self.params.square_side \
                          + self.params.square_side // 2
            self._canvas.create_text(left_offset, top_row_top_offset, text=file,
                                     **self.params.marks_params)
            self._canvas.create_text(left_offset, lower_row_top_offset, text=file,
                                     **self.params.marks_params)

    def _fill_squares(self):
        for i in range(self.SIZE):
            for j in range(self.SIZE):
                left_offset = self.params.board_offset + self.params.square_side * i
                top_offset = self.params.board_offset + self.params.square_side * j
                square_colour = self.params.white_colour if (i + j) % 2 == 0 \
                    else self.params.black_colour
                self._canvas.create_rectangle(
                    left_offset + self.params.line_width // 2,
                    top_offset + self.params.line_width // 2,
                    left_offset + self.params.square_side - self.params.line_width // 2,
                    top_offset + self.params.square_side - self.params.line_width // 2,
                    fill=square_colour, outline="")

    def _draw_pieces(self):
        for i in range(self.SIZE):
            for j in range(self.SIZE):
                piece = self._board[indexes_to_notation(self.SIZE - j - 1, i)]
                if piece is not None:
                    piece_x = self.params.board_offset + self.params.square_side * i \
                              + self.params.square_side // 2
                    piece_y = self.params.board_offset + self.params.square_side * j \
                              + self.params.square_side // 2
                    self._canvas.create_text(piece_x, piece_y, text=piece.symbol,
                                             **self.params.pieces_params)

