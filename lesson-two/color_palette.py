import curses
import random

def screen(stdscr):

    # turn off the cursor.
    curses.curs_set(0)

    # set the block character
    # ✸ 10040 ❂ 10050 ✹ 10041
    # █ 9608 ◼ 9724
    # ⚑ 9873 ⚐ 9872
    block = chr(9608)
    # set the block column and rows
    block_c = 4
    block_r = 1

    # initialize the color pair
    curses.start_color()
    curses.use_default_colors()
    color_perrow = 16

    for i in range(0, curses.COLORS):
    #for i in range(0, 20):
        # pair number, foreground color, background color
        curses.init_pair(i + 1, i, -1)
        the_color = curses.color_pair(i + 1)

        # calculate the y-axis.
        y = i // color_perrow
        # calculate the x-axis.
        x = i % color_perrow

        #stdscr.addstr("<{0}>".format(i + 1), curses.color_pair(i + 1))
        # the ragne will inclue the first one not the last number
        # paint the color blocks
        for xi in range(x * block_c, x * block_c + block_c):
            for yi in range(y * (block_r + 1), y * (block_r + 1) + block_r):
                stdscr.addstr(yi, xi, block, the_color)
        
        # paint the color pair id.
        stdscr.addstr(y * (block_r + 1) + block_r, x * block_c, str(i + 1), the_color)

    # hold the window until user type any key.
    stdscr.getch()

curses.wrapper(screen)
