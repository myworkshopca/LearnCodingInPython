import curses
from curses import textpad
import random

def main(stdscr):

    curses.start_color()
    curses.use_default_colors()
    # set pair 1 to green.
    curses.init_pair(1, 46, -1)
    # set pair 2 to red
    curses.init_pair(2, 196, -1)

    # set 0 to disable the flash.
    curses.curs_set(0)
    # set up this to make the while loop work.
    stdscr.nodelay(1)
    # timeout is using millisecond (ms) as unit
    stdscr.timeout(50)

    # get the size of the windown.
    sh, sw = stdscr.getmaxyx()
    # set the center. [y-axis, x-axis]
    center = [sh // 2, sw // 2]

    # set up the game area.
    # top left and bottom right
    box = [
        [3, 3],
        [sh - 3, sw - 3]
    ]
    # draw the rectangle as the game area.
    textpad.rectangle( stdscr, box[0][0], box[0][1], box[1][0], box[1][1])

    # define the snake, starts with 3 unit.
    # the first will be the head of the snake
    # and the last will be the tail of the snake.
    snake = [
        # the heading unit
        [center[0], center[1] + 1],
        center,
        # the tailing unit
        [center[0], center[1] - 1],
    ]

    # draw the snake
    for point in snake:
        #stdscr.addstr(point[0], point[1], "#", curses.color_pair(1))
        stdscr.addstr(point[0], point[1], chr(9724), curses.color_pair(1))

    # set direction for the snake. we will use key to set the direction.
    # we will start with moving to right
    direction = curses.KEY_RIGHT

    # produce snake food, it will have format [y-axis, x-axis]
    # generate random number to decide the location of the snake food.
    # one food each time.
    food = [
        # the y axis
        random.randint(box[0][0] + 1, box[1][0] - 1),
        # the x axis
        random.randint(box[0][1] + 1, box[1][1] - 1)
    ]
    stdscr.addstr(food[0], food[1], "*", curses.color_pair(2))

    # set the initial score to 0
    score = 0

    # keep the snake moveing.
    # - while infinity loop to keep the snake moving.
    # - move the snake by adding one heading unit and removing the tailing unit.
    # - the direction will decide where to add the heading unit:
    #   up, down, right or left
    # how we handle food?
    # - the snake will eat the food if its head move to the same unit of food
    # - the sname will grow one unit after eat one food,
    #   simply not remove the tailing unit.
    while 1:
        # we need this for timeout to work.
        user_key = stdscr.getch()

        # get the current head.
        head = snake[0]

        # decide the direction based on the food position and
        # the snake head
        # decide the y-axis
        if head[0] < food[0]:
            direction = curses.KEY_DOWN
        elif head[0] > food[0]:
            direction = curses.KEY_UP
        elif head[1] < food[1]:
            # the x-axis
            direction = curses.KEY_RIGHT
        elif head[1] > food[1]:
            direction = curses.KEY_LEFT

        # we will keep the existing direction for all other keys.

        # decide the new head based on the direction
        if direction == curses.KEY_UP:
            newHead = [head[0] - 1, head[1]]
        elif direction == curses.KEY_DOWN:
            newHead = [head[0] + 1, head[1]]
        elif direction == curses.KEY_RIGHT:
            newHead = [head[0], head[1] + 1]
        elif direction == curses.KEY_LEFT:
            newHead = [head[0], head[1] - 1]

        # draw the new head.
        #stdscr.addstr(newHead[0], newHead[1], "#")
        stdscr.addstr(newHead[0], newHead[1], chr(9724), curses.color_pair(1))
        # add the new head to snake body.
        snake.insert(0, newHead)

        # after add new head, we will decide if we will remove the tail or not
        # depends on the food.
        if snake[0] == food:
            # increase scored
            score += 1
            # produce new food.
            food = [
                # the y axis
                random.randint(box[0][0] + 1, box[1][0] - 1),
                # the x axis
                random.randint(box[0][1] + 1, box[1][1] - 1)
            ]
            # draw the new food on board.
            stdscr.addstr(food[0], food[1], "*", curses.color_pair(2))
            # TODO: make it faster by reduce the timeout time.
        else:
            # remove the tailing unit of the snake, by draw an empty string.
            stdscr.addstr(snake[-1][0], snake[-1][1], " ")
            # remove the tailing unit from the snake body.
            snake.pop()

        # Game over conditions
        if (snake[0][0] in [box[0][0], box[1][0]] or
            snake[0][1] in [box[0][1], box[1][1]]):

            msg = "Game Over! Press any key to exit!"
            stdscr.addstr(center[0], center[1] - len(msg)//2, msg)
            # turn off the nodelay mode.
            stdscr.nodelay(0)
            # wait for user's input
            stdscr.getch()
            break

curses.wrapper(main)
