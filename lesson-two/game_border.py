import curses

def main(stdscr):

    # turn off the cursor
    curses.curs_set(0)

    sh, sw = stdscr.getmaxyx()
    msg = "Welcome to keyboard encoding game"
    # print the welcome message y-axis and x-axis
    stdscr.addstr(3, sw // 2 - len(msg) // 2, msg)
    # how to play.
    msg = "Press any key to show the result and Press ESC to exit!"
    stdscr.addstr(4, sw // 2 - len(msg) // 2, msg, curses.COLOR_GREEN)

    # paint the border.
    # the top and bottom border.
    margin = 5 
    border_ch = "*"
    while True:
        userType = stdscr.getch()
        if userType == 27:
            break
        elif userType == ord(border_ch):
            continue
        else:
            border_ch = chr(userType)
            for x in range(margin, sw - margin):
                stdscr.addstr(margin, x, border_ch)
                stdscr.addstr(sh - margin, x, border_ch)
        
            for y in range(margin, sh - margin + 1):
                stdscr.addstr(y, margin, border_ch)
                stdscr.addstr(y, sw - margin, border_ch)

curses.wrapper(main)
