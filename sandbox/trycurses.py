import curses
from curses import textpad

def main(stdscr):

    # set 0 to disable the flash.
    curses.curs_set(0)
    # set up this to make the while loop work.
    stdscr.nodelay(1)
    stdscr.timeout(100)

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
    # the first will be the head of the snake
    # and the last will be the tail of the snake.
    snake = [
        [sh // 2, sw // 2 + 1],
        [sh // 2, sw // 2],
        [sh // 2, sw // 2 - 1]
    ]

    #draw the snake
    for point in snake:
        stdscr.addstr(point[0], point[1], "#")

    # move the snake
    while 1:

        # we need this for timeout to work.
        stdscr.getch()

        # get the current head.
        head = snake[0]
        # decide the new head.
        newHead = [head[0], head[1] + 1]
        # draw the new head.
        #stdscr.addstr(newHead[0], newHead[1], "#")
        stdscr.addstr(newHead[0], newHead[1], "#")
        # add the new head to snake body.
        snake.insert(0, newHead)
        # remove the tailing unit of the snake, by draw an empty string.
        stdscr.addstr(snake[-1][0], snake[-1][1], " ")
        # remove the tailing unit from the snake body.
        snake.pop()

    ## add message for exit game.
    #exitMsg = 'Press any key to exit!'
    #stdscr.addstr(sh - 2, center[1] - len(exitMsg) // 2, exitMsg)

    #stdscr.refresh()

    ## waiting for user input
    #stdscr.getch()

curses.wrapper(main)
