import curses

def main(stdscr):

    # turn off the cursor
    curses.curs_set(0)

    curses.start_color()
    curses.use_default_colors()
    # set pair 1 to green.
    curses.init_pair(1, 46, -1)
    # set pair 2 to red
    curses.init_pair(2, 196, -1)

    # get the size of the window
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
    # use red as the border color
    border_color = curses.color_pair(2)
    # set green as the message color.
    msg_color = curses.color_pair(1)
    while True:
        userType = stdscr.getch()
        if userType == 27:
            break
        elif userType == ord(border_ch):
            continue
        else:
            border_ch = chr(userType)
            # paint the border.
            for x in range(margin, sw - margin):
                stdscr.addstr(margin, x, border_ch, border_color)
                stdscr.addstr(sh - margin, x, border_ch, border_color)
        
            for y in range(margin, sh - margin + 1):
                stdscr.addstr(y, margin, border_ch, border_color)
                stdscr.addstr(y, sw - margin, border_ch, border_color)
            # show the message at the center.
            user_msg = "You typed {0}, ASCII code: {1}".format(chr(userType), userType)
            stdscr.addstr(sh // 2, sw // 2 - len(user_msg) // 2, user_msg, msg_color)

curses.wrapper(main)
