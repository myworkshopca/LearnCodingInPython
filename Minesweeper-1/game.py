import curses

def initfield(stdscr, center, size):

  for y in range(center[0] - size[0] // 2, center[0] + size[0] // 2):
    for x in range(center[1] - size[1], center[1] + size[1], 2):
      stdscr.addstr(y, x, chr(9608))

def square(stdscr):

  curses.curs_set(0)

  sh, sw = stdscr.getmaxyx()
  center = [sh // 2, sw // 2]

  # row, column pair
  size = [16, 50]

  initfield(stdscr, center, size)

  stdscr.getch()

curses.wrapper(square)
