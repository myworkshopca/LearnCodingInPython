import curses

def main(stdscr):

    sh, sw = stdscr.getmaxyx()
    # y-axis and x-axis
    stdscr.addstr(sh // 2, sw // 2, 'Welcome to snake game!')

    stdscr.getch()

curses.wrapper(main)
