from curses import textpad
import curses

def main(stdscr):

    # set 0 to disable the flash.
    curses.curs_set(0)

    # get the size of the windown.
    sh, sw = stdscr.getmaxyx()

    # set up the game area.
    # top left and bottom right
    box = [[3,3], [sh - 3, sw - 3]]
    # draw the rectangle as the game area.
    textpad.rectangle( stdscr, box[0][0], box[0][1], box[1][0], box[1][1])

    stdscr.refresh()

    # waiting for user input
    stdscr.getch()

curses.wrapper(main)
