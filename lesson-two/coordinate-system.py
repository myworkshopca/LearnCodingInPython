import curses

def window(stdscr):

    curses.curs_set(0)

    # get size of the screen.
    sh, sw = stdscr.getmaxyx()

    # ┌ 9484
    stdscr.addstr(0, 0, chr(9484))

    # paint the x axis.
    for x in range(1, sw):
        # ─ 9472
        stdscr.addstr(0, x, chr(9472))
    # paint the ending 9658 - ►
    stdscr.addstr(0, sw - 1, chr(9658))

    for y in range(1, sh):
        # │ 9474
        stdscr.addstr(y, 0, chr(9474))
    # paint the ending ▼ 9660
    stdscr.addstr(sh - 1, 0, chr(9660))

    stdscr.getch()

curses.wrapper(window)
