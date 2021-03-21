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

    # turn off default cursor
    curses.curs_set(False)

    # set this variable to track nodelay or not.
    nodelay = True
    stdscr.nodelay(nodelay)
    # timeout is on millionsecond
    nodelay_timeout = 200
    stdscr.timeout(nodelay_timeout)

    sh, sw = stdscr.getmaxyx()

    # set margin.
    m_y, m_x = 2, 5
    # new margin
    n_y, n_x = 2, 5
    # set the border character.
    # ֍ 🄂🊭 🈪
    # 🨄  🩡
    # ❶ 10102 ⓵  9461
    # █ 9608 ◼ 9724
    # ▩ 9641
    # ⬤  11044
    # ✶ 10038, ✹ 10041, ✴ 10036, ✡ 10017
    # ⊚ 8858 ⊙ 8857
    # ● 9679 ◉ 9673 ⚫ 9899
    # ⓫ 9451
    # ❎ 10062
    # ✖ 10006
    # 🏿 127999
    # ⑤ 9316
    # ⊞ 8862
    border_ch = chr(127999)

    while 1:
        # collect user's input.
        user_key = stdscr.getch()

        # exit when user press ESC q or Q
        if user_key in [27, ord('q'), ord('Q')]:
            break
        elif user_key in [ord(' ')]:
            # using white space to perform pause and resume.
            if nodelay:
                nodelay = False
                stdscr.nodelay(nodelay)
                nodelay_timeout = -1
                stdscr.timeout(nodelay_timeout)
            else:
                nodelay = True
                stdscr.nodelay(nodelay)
                nodelay_timeout = 120
                stdscr.timeout(nodelay_timeout)

        # calculate the new margin.
        n_y = m_y + 1
        n_x = m_x + 1

        # erase the old border
        paint_border(stdscr, m_y, m_x, sh - m_y, sw - m_x, " ")
        # paint the new border
        paint_border(stdscr, n_y, n_x, sh - n_y, sw - n_x, border_ch)
        # reset the new border
        m_y, m_x = n_y, n_x

curses.wrapper(border)
