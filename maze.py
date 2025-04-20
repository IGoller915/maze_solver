from cell import *
import time

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_cols,
        num_rows,
        cell_size_x,
        cell_size_y,
        win = None,
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win

        self._create_cells()

    def _create_cells(self):
        self._cells = []
        for i in range(self._num_cols):
            self._cells.append([])
            for j in range(self._num_rows):
                self._cells[i].append(Cell(self._win))
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self.cell_size_x
        x2 = self._x1 + (i + 1) * self.cell_size_x
        y1 = self._y1 + j * self.cell_size_y
        y2 = self._y1 + (j + 1) * self.cell_size_y
        self._cells[i][j].draw(x1, x2, y1, y2)

        self._animate()
    
    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.005)
    
    def _break_entrance_and_exit(self):
        tl_cell = self._cells[0][0]
        tl_cell.has_top_wall = False
        self._draw_cell(0, 0)

        br_cell = self._cells[self._num_cols - 1][self._num_rows - 1]
        br_cell.has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)