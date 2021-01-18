import curses

def main(stdscr):
  # turn off cursor blinking by set to 0
  # set to 0 to turn on it.
  curses.curs_set(0)

  # get the screen size
  sh, sw = stdscr.getmaxyx()
  # figure out the center of the screen.
  # the operator // will return integer compare to /
  center = [sh // 2, sw // 2]
  
  text = 'Hello Curses World!'
  stdscr.addstr(center[0], center[1] - len(text) // 2, text)

  hintMessage = 'Press    any     key     to    exit'
  stdscr.addstr(sh - 2, center[1] - len(hintMessage) // 2, hintMessage)

  stdscr.refresh()
  stdscr.getch()

curses.wrapper(main)
