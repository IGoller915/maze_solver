from cell import *
import time
import random

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
        seed = None
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        if seed != None:
            random.seed(seed)

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

        # self._animate()
    
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

    def _break_walls_r(self, i, j):
        current_cell = self._cells[i][j]
        current_cell.visited = True
        while True:
            to_visit = []
            adjacent = [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]
            for cell in adjacent:
                if 0 <= cell[0] < self._num_cols and 0 <= cell[1] < self._num_rows and self._cells[cell[0]][cell[1]].visited == False:
                    to_visit.append(cell)
            if to_visit == []:
                self._draw_cell(i, j)
                return
            else:
                direction = random.randrange(0, len(to_visit))
                new_coords = to_visit[direction]
                new_cell = self._cells[new_coords[0]][new_coords[1]]
            if new_coords[0] < i:
                current_cell.has_left_wall = False
                new_cell.has_right_wall = False
            if new_coords[0] > i:
                current_cell.has_right_wall = False
                new_cell.has_left_wall = False
            if new_coords[1] < j:
                current_cell.has_top_wall = False
                new_cell.has_bottom_wall = False
            if new_coords[1] > j:
                current_cell.has_bottom_wall = False
                new_cell.has_top_wall = False

            self._break_walls_r(new_coords[0], new_coords[1])