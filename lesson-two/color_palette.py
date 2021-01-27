import curses
import random

def screen(stdscr):

    # turn off the cursor.
    curses.curs_set(0)

    # initialize the color pair
    curses.start_color()
    curses.use_default_colors()
    for i in range(0, curses.COLORS):
        # pair number, foreground color, background color
        curses.init_pair(i + 1, i, -1)
        stdscr.addstr("<{0}>".format(i + 1), curses.color_pair(i + 1))

    stdscr.getch()

curses.wrapper(screen)
