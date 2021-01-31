import curses

def main(stdscr):

    sh, sw = stdscr.getmaxyx()
    msg = "Welcome to keyboard encoding"
    # print the welcome message y-axis and x-axis
    stdscr.addstr(0, sw // 2 - len(msg) // 2, msg)

    # paint the border.
    # the top and bottom border.
    for x in range(0, sw - 1):
        stdscr.addstr(2, x, '+')
        stdscr.addstr(sh - 3, x, '+')

    for y in range(0, sh - 1):
        stdscr.addstr(y, 1, "|")
        stdscr.addstr(y, sw - 1, "|")

    stdscr.getch()

curses.wrapper(main)
