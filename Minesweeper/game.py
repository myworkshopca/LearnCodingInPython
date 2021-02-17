import curses
import random

def sweeper(stdscr):

    # set 0 to hide the cursor.
    curses.curs_set(0)

    # get the size of the windown.
    sh, sw = stdscr.getmaxyx()
    # set the center. [y-axis, x-axis]
    center = [sh // 2, sw // 2]

    # define the char for cell ◼ is 9724
    cell_ch = chr(9724)

    # paint the minefield.
    # set size of the field.
    field_size = 10
    # the initial mine field with 2 cells in the first row.
    field = [[[0,0]] * field_size] * field_size
    # using row (r) and column (c) for index.
    r, c = 0, 0
    # we paint the row (y-axis) one after another.
    for y in range(center[0] - field_size, center[0] + field_size):
        # we paint the column (x-axis) with one cell empty
        for x in range(center[1] - field_size * 2, center[1] + field_size * 2, 2):
            #print('r={}, c={}'.format(r,c))
            #field[r][c] = [y, x]
            stdscr.addstr(y, x, cell_ch)
            # increase the column index.
            c = c + 1
        # increase the row.
        r = r + 1

    # paint the reverse cell for the first cell.
    stdscr.addstr(field[0][0][0], field[0][0][1], cell_ch, curses.A_REVERSE)

    # try move the cursors
    #while True:


    stdscr.getch()

curses.wrapper(sweeper)
