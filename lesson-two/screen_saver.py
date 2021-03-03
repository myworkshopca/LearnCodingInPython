import curses
from curses import textpad
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
    # set the center. [y-axis, x-axis]
    center = [sh // 2, sw // 2]

    # set the welcome message.
    welcome_msg = 'Random Letters Screen Saver'
    stdscr.addstr(1, center[1] - len(welcome_msg) // 2, welcome_msg)
    # paint the welcome message.
    welcome_msg = 'ESC key to exist!'
    stdscr.addstr(2, center[1] - len(welcome_msg) // 2, welcome_msg)
    # set up the game area.
    # top left and bottom right
    box = [
        [3, 3],
        [sh - 3, sw - 3]
    ]
    # draw the rectangle as the game area.
    textpad.rectangle( stdscr, box[0][0], box[0][1], box[1][0], box[1][1])

    # set up this to make the while loop work.
    stdscr.nodelay(1)
    # timeout is using millisecond (ms) as unit
    stdscr.timeout(100)

    while True:
        y = random.randint(4, sh - 4)
        x = random.randint(4, sw - 4)
        
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
