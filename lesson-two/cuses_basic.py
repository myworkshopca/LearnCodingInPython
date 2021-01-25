import curses

def main(stdscr):

    sh, sw = stdscr.getmaxyx()
    msg = "Welcome to snake game" * 2
    # y-axis and x-axis
    stdscr.addstr(sh // 2, sw // 2 - len(msg) // 2, msg)

    stdscr.getch()

curses.wrapper(main)
