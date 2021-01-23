import curses

def main(stdscr):

    curses.curs_set(1)

    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, 46, -1)

    # set 0 to turn off the nodelay mode.
    # we will wait for user's input.
    stdscr.nodelay(0);

    # the y axis, starts from 1
    y = 1
    # print the prompt message:
    stdscr.addstr(0, 0, 'Process Q to exit!')
    while 1:

        userType = stdscr.getch()
        # getch will return a ascii code for each key,
        # the function chr to conver a ascii code to a character
        msg = "{0} - {1}".format(userType, chr(userType))
        stdscr.addstr(y, 1, msg, curses.color_pair(1));
        y += 1
        if chr(userType) == 'Q':
            break

    # promote the exit message!
    stdscr.addstr(y, 1, 'Closing game ...')

    # turn on the nodelay mode so we could use timeout
    stdscr.nodelay(1)
    # timeout in ms
    stdscr.timeout(800)
    # call getch in nodelay mode to show the message.
    stdscr.getch()

curses.wrapper(main)
