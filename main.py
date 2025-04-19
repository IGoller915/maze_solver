from graphics import *
from cell import *

def main():
    win = Window(800, 600)

    
    for i in range(0, 16):
        for j in range(0, 12):
            cell = Cell(win)
            cell.draw(i*50,i*50+50,j*50,j*50+50)

    win.wait_for_close()
main()