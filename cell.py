from graphics import *

class Cell:
    def __init__(self, win = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

        self.visited = False

    def draw(self, x1, x2, y1, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, "white")
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, "white")
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, "white")
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, "white")
    
    def draw_move(self, to_cell, undo=False):
        self.x_center = (self._x1 + self._x2) / 2
        self.y_center = (self._y1 + self._y2) / 2
        to_cell.x_center = (to_cell._x1 + to_cell._x2) / 2
        to_cell.y_center = (to_cell._y1 + to_cell._y2) / 2

        line = Line(Point(self.x_center, self.y_center), Point(to_cell.x_center, to_cell.y_center))
        fill_color = "red"
        if undo == False:
            fill_color = "grey"
        
        self._win.draw_line(line, fill_color)