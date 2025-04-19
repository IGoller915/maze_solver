from graphics import *
from cell import *

def main():
    win = Window(800, 600)

    
    # for i in range(0, 16):
    #     for j in range(0, 12):
    #         cell = Cell(win)
    #         cell.draw(i*50,i*50+50,j*50,j*50+50)

    cell1 = Cell(win)
    cell2 = Cell(win)
    cell1.draw(50,97,50,97)
    cell2.draw(300,350,300,350)
    cell1.draw_move(cell2, True)

    win.wait_for_close()
main()