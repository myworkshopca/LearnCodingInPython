import curses

def window(stdscr):

    curses.curs_set(0)

    # get size of the screen.
    sh, sw = stdscr.getmaxyx()

    # paint the x axis.
    for x in range(0, sw):
        stdscr.addstr(0, x, "-")
    # paint the ending 9658 - ►
    stdscr.addstr(0, sw - 1, chr(9658))

    for y in range(0, sh):
        stdscr.addstr(y, 0, "|")
    # paint the ending "▼"
    stdscr.addstr(sh - 1, 0, chr(9660))

    stdscr.getch()

curses.wrapper(window)
