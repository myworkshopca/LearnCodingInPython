from curses import textpad
import curses

def main(stdscr):

    # set 0 to disable the flash.
    curses.curs_set(0)

    # get the size of the windown.
    sh, sw = stdscr.getmaxyx()
    # set the center.
    center = [sh // 2, sw // 2]

    # set up the game area.
    # top left and bottom right
    box = [
        [3, 3],
        [sh - 3, sw - 3]
    ]
    # draw the rectangle as the game area.
    textpad.rectangle( stdscr, box[0][0], box[0][1], box[1][0], box[1][1])

    # define the snake.
    snake = [
        [sh // 2, sw // 2 + 1],
        [sh // 2, sw // 2],
        [sh // 2, sw // 2 - 1]
    ]

    #draw the snake
    for point in snake:
        stdscr.addstr(point[0], point[1], "#")
    
    # add message for exit game.
    exitMsg = 'Press any key to exit!'
    stdscr.addstr(sh - 2, center[1] - len(exitMsg) // 2, exitMsg)

    stdscr.refresh()

    # waiting for user input
    stdscr.getch()

curses.wrapper(main)
