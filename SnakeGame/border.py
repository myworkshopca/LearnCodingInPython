import curses

def paint_border(stdscr, uly, ulx, lry, lrx, border_ch):

    # paint the top and bottom border, loop x-axis.
    # range includes the start number, but NOT include end number.
    for x in range(ulx, lrx + 1):
        # the top border.
        stdscr.addstr(uly, x, border_ch)
        # the bottom border.
        stdscr.addstr(lry, x, border_ch)

    # loop through y-axis, paint the left and right border.
    for y in range(uly, lry + 1):
        # paint the left border.
        stdscr.addstr(y, ulx, border_ch)
        # paint the right border.
        stdscr.addstr(y, lrx, border_ch)

def border(stdscr):

    curses.curs_set(0)

    sh, sw = stdscr.getmaxyx()

    # set margin.
    margin_y = 2
    margin_x = 5
    # set the border character.
    # █ 9608 ◼ 9724
    border_ch = chr(9608)

    paint_border(stdscr, margin_y, margin_x, sh - margin_y, sw - margin_x, border_ch)
    stdscr.getch()
    paint_border(stdscr, margin_y, margin_x, sh - margin_y, sw - margin_x, " ")
    stdscr.getch()

curses.wrapper(border)
