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

    # get screen height and width.
    sh, sw = stdscr.getmaxyx()

    # set up this to make the while loop work.
    stdscr.nodelay(1)
    # timeout is using millisecond (ms) as unit
    stdscr.timeout(100)

    while True:
        y = random.randint(0, sh - 1)
        x = random.randint(0, sw - 1)
        
        # get the random character
        char = random.randint(32, 126)
        # get the random color
        color = random.randint(1, curses.COLORS + 1)

        stdscr.addstr(y, x, chr(char), curses.color_pair(color))

        userType = stdscr.getch()
        # ESC key is 27
        # process ESC key to exit.
        if userType == 27:
            break

curses.wrapper(screen)
