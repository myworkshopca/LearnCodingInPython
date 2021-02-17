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
    field_size = 10
    #field = 
    for y in range(center[0] - field_size, center[0] + field_size):
        for x in range(center[1] - field_size * 2, center[1] + field_size * 2, 2):
            stdscr.addstr(y, x, cell_ch)

    stdscr.getch()

curses.wrapper(sweeper)
