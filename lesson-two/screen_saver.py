import curses
import random

def screen(stdscr):

    # turn off the cursor.
    curses.curs_set(0)
    # set up this to make the while loop work.
    stdscr.nodelay(1)
    # timeout is using millisecond (ms) as unit
    stdscr.timeout(100)

    # get screen height and width.
    sh, sw = stdscr.getmaxyx()

    while True:
        y = random.randint(0, sh - 1)
        x = random.randint(0, sw - 1)

        stdscr.addstr(y, x, "@")

        userType = stdscr.getch()
        if chr(userType) == "Q":
            break

curses.wrapper(screen)
