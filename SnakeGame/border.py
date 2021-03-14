import curses

def border(stdscr):

    sh, sw = stdscr.getmaxyx()

    # set margin.
    margin_y = 2
    margin_x = 5
    # set the border character.
    # █ 9608 ◼ 9724
    border_ch = chr(9608)

    # paint the top and bottom border, loop x-axis.
    for x in range(margin_x, sw - margin_x):
        # the top border.
        stdscr.addstr(margin_y, x, border_ch)
        # the bottom border.
        stdscr.addstr(sh - margin_y, x, border_ch)

    # loop through y-axis, paint the left and right border.
    for y in range(margin_y, sh - margin_y):
        # paint the left border.
        stdscr.addstr(y, margin_x, border_ch)
        # paint the right border.
        stdscr.addstr(y, sw - margin_x, border_ch)

    stdscr.getch()

curses.wrapper(border)
