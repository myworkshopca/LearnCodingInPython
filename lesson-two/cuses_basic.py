import curses

def main(stdscr):

    # turn off the cursor
    curses.curs_set(0)

    sh, sw = stdscr.getmaxyx()
    msg = "Welcome to keyboard encoding game"
    # print the welcome message y-axis and x-axis
    stdscr.addstr(1, sw // 2 - len(msg) // 2, msg)

    # paint the border.
    # the top and bottom border.
    margin = 10
    border_ch = "*"
    for x in range(margin, sw - margin):
        stdscr.addstr(margin, x, border_ch)
        stdscr.addstr(sh - margin, x, border_ch)

    for y in range(margin, sh - margin + 1):
        stdscr.addstr(y, margin, border_ch)
        stdscr.addstr(y, sw - margin, border_ch)

    stdscr.getch()

curses.wrapper(main)
