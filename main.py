from graphics import *
from cell import *
from maze import *

def main():
    num_rows = 40
    num_cols = 50
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)
    seed = None

    maze = Maze(margin, margin, num_cols, num_rows, cell_size_x, cell_size_y, win, seed)
    maze._break_entrance_and_exit()
    maze._break_walls_r(0, 0)
    maze._reset_cells_visited()
    maze.solve()

    win.wait_for_close()
main()