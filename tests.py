import unittest
from maze import *

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_cols, num_rows, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_reset_visited(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_cols, num_rows, 10, 10)
        m1._break_entrance_and_exit()
        m1._break_walls_r(0, 0)
        m1._reset_cells_visited()
        for i in range(m1._num_cols):
            for j in range(m1._num_rows):
                self.assertEqual(
                    m1._cells[i][j].visited,
                    False,
                )

if __name__ == "__main__":
    unittest.main()