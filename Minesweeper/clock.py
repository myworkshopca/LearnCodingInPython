import curses
import datetime

def clock(stdscr):

    # set 0 to hide the cursor.
    curses.curs_set(0)
    # set up this to make the while loop work.
    stdscr.nodelay(1)
    # timeout is using millisecond (ms) as unit
    stdscr.timeout(1000)
    
    while True:

        userkey = stdscr.getch()

        if userkey in [27, 113, 81]:
            break;

        stdscr.addstr(0, 0, str(datetime.datetime.now()))

curses.wrapper(clock)
