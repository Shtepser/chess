from __future__ import annotations
from tkinter import Frame, Canvas, Event

from board import Board
from tkinter_gui.SelectedPiece import SelectedPiece
from utils import indexes_to_notation, notation_to_indexes


class BoardView(Frame):
    SIZE = 8

    class BoardViewParams:

        _LINE_WIDTH_COEFFICIENT = 0.05
        _OFFSET = 10
        _COORDINATES_WIDTH = 25
        _BOARD_OFFSET = _OFFSET + _COORDINATES_WIDTH
        _WHITE_SQUARES_COLOUR = "#f0a12e"
        _BLACK_SQUARES_COLOUR = "#8e2d1e"
        _MARKS_FONT = "Roman"
        _MARKS_FONT_SIZE = 14
        _PIECES_FONT = "Arial"
        _PIECES_FONT_SIZE = 40
        _POSSIBLE_MOVES_COLOUR = "#5c75ff"
        _POSSIBLE_ATTACKS_COLOUR = "#755d9a"
        _POSSIBLE_TURNS_SIZE = 23

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

        @property
        def possible_turns_size(self):
            return self._POSSIBLE_TURNS_SIZE

        @property
        def possible_moves_colour(self):
            return self._POSSIBLE_MOVES_COLOUR

        @property
        def possible_attacks_colour(self):
            return self._POSSIBLE_ATTACKS_COLOUR

        @property
        def possible_turns_params(self):
            return {"outline": ""}

    def __init__(self, board: Board, selected_piece: SelectedPiece, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._board = board
        self._canvas = Canvas(self)
        self._canvas.grid(column=0, row=0)
        self._canvas.bind("<Button-1>", self.clicked)
        self._canvas.configure(width=500, height=500)
        self._selected_piece = selected_piece
        self.redraw()

    def clicked(self, event: Event):
        clicked_row = (event.y - self.params.board_offset) // self.params.square_side
        clicked_col = (event.x - self.params.board_offset) // self.params.square_side
        if 0 <= clicked_row < self.SIZE and 0 <= clicked_col < self.SIZE:
            clicked_square = indexes_to_notation(self.SIZE - clicked_row - 1,
                                                 clicked_col)
            self.event_generate("<<Square-Clicked>>",
                                data={"clicked_square": clicked_square})

    def redraw(self):
        self.update_params()
        self._clear_canvas()
        self._draw_grid()
        self._draw_marks()
        self._fill_squares()
        self._draw_pieces()
        if self._selected_piece.is_set():
            self._draw_possible_moves()

    def update_params(self):
        super().update()
        self.params = BoardView.BoardViewParams(self._canvas, self.SIZE)

    def update(self):
        super().update()
        self.redraw()

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

    def _draw_possible_moves(self):
        for move in self._selected_piece.possible_moves():
            row, col = notation_to_indexes(move)
            row = self.SIZE - row - 1
            left_corner = self.params.board_offset + col * self.params.square_side \
                          + self.params.square_side // 2 \
                          - self.params.possible_turns_size // 2
            upper_corner = self.params.board_offset + row * self.params.square_side \
                           + self.params.square_side // 2 \
                           - self.params.possible_turns_size // 2
            fill = self.params.possible_moves_colour \
                if move in self._selected_piece.possible_ordinary_moves() \
                else self.params.possible_attacks_colour
            self._canvas.create_oval(left_corner, upper_corner,
                                     left_corner + self.params.possible_turns_size,
                                     upper_corner + self.params.possible_turns_size,
                                     fill=fill,
                                     **self.params.possible_turns_params)

