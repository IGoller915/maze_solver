from graphics import *

def main():
    win = Window(800, 600)
    point1 = Point(32, 64)
    point2 = Point(546, 347)
    point3 = Point(786, 345)
    line1 = Line(point1, point2)
    line2 = Line(point1, point3)
    line3 = Line(point2, point3)
    win.draw_line(line1, "blue")
    win.draw_line(line2, "blue")
    win.draw_line(line3, "blue")
    win.wait_for_close()


main()