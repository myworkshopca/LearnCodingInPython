import curses
import random

def sweeper(stdscr):

    # get the size of the windown.
    sh, sw = stdscr.getmaxyx()
    # set the center. [y-axis, x-axis]
    center = [sh // 2, sw // 2]

    # define the char for cell
    cell_ch = chr(9786)

    # define the minefield.
    #field = 
    for y in range(center[0] - 5, center[0] + 5):
        for x in range(center[1] - 5, center[1] + 5):
            stdscr.addstr(y, x, cell_ch)

    stdscr.getch()

curses.wrapper(sweeper)
