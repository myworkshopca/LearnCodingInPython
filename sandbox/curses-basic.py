import curses

def main(stdscr):

    curses.curs_set(1)

    # set 0 to turn off the nodelay mode.
    # we will wait for user's input.
    stdscr.nodelay(0);

    # the y axis, starts from 1
    y = 1
    while 1:

        userType = stdscr.getch()
        # getch will return a ascii code for each key,
        stdscr.addstr(y, 1, chr(userType));
        y += 1

curses.wrapper(main)
