import curses
import math
import random

def initfield(center, size):

  # the field variable to store all cells.
  field = []

  # using row (r) and column (c) for index
  r = 0
  # nested loop
  for y in range(center[0] - size[0] // 2, center[0] + size[0] // 2):
    # initialize each row.
    # repeat the size of column
    field.append([]);
    for x in range(center[1] - size[1], center[1] + size[1], 2):
      field[r].append([y, x, 0, 'covered'])
      #stdscr.addstr(y, x, chr(9608))
      # done one column in a row.
      # increase the column index.
    # done one row. increase the row index.
    r = r + 1

  # generate the bombs! by 15% of the field cells
  # set variable i to count bombs
  i = 0
  while i < math.prod(size) // 7:
      index = random.randint(0, math.prod(size) - 1)
      # divide the column size will be the row.
      r = index // size[1]
      c = index - r * size[1]
      if field[r][c][2] == -1:
          # there is already a bomb in this cell.
          continue
      else:
          # set the number of bombs to -1
          field[r][c][2] = -1;
          # increase the count.
          i = i + 1

  # calculate the number of bombs in surrounding cells.
  for y in range(0, size[0]):
      for x in range(0, size[1]):
          if field[y][x][2] == -1:
              # this cell buried a bomb. skip
              continue

          for sy in [y - 1, y, y + 1]:
              for sx in [x - 1, x, x + 1]:
                  if (sy < 0 or sy >= size[0] or
                      sx < 0 or sx >= size[1]):
                      # out of bound
                      continue
                  elif sy == y and sx == x:
                      # skip current cell.
                      continue
                  else:
                      if field[sy][sx][2] == -1:
                          # this surrounding cell is a bomb!
                          field[y][x][2] += 1

  # return the field!
  return field

def paintfield(stdscr, field, size, colors, show=False):

    for r in range(0, size[0]):
        for c in range(0, size[1]):
            paintcell(stdscr, field[r][c], colors, False, show)

def paintcell(stdscr, cell, colors, reverse=False, show=False):

    # decide the character and color.
    cell_ch = chr(9608)
    cell_color = colors['cover']

    if show:
        cell_ch = str(cell[2])
        cell_color = colors[str(cell[2])]
    if show and cell[2] == -1:
        cell_ch = chr(10041)

    # check reverse or not!
    if reverse:
        cell_color = curses.A_REVERSE

    # paint the cell.
    stdscr.addstr(cell[0], cell[1], cell_ch, cell_color)

"""
initialize curses colors and return the color dictionary.
"""
def colordict():

    curses.start_color()
    curses.use_default_colors()
    for i in range(0, curses.COLORS):
        curses.init_pair(i + 1, i, -1)

    return{
        'cover': curses.color_pair(9),
        'flag': curses.color_pair(12),
        '-1': curses.color_pair(53),
        '0': curses.color_pair(1),
        '1': curses.color_pair(13),
        '2': curses.color_pair(48),
        '3': curses.color_pair(10),
        '4': curses.color_pair(52),
        '5': curses.color_pair(94),
        '6': curses.color_pair(203),
        '7': curses.color_pair(90),
        '8': curses.color_pair(178)
    }

def square(stdscr):

    curses.curs_set(0)

    colors = colordict()
    sh, sw = stdscr.getmaxyx()
    center = [sh // 2, sw // 2]

    # row, column pair
    size = [20, 50]

    field = initfield(center, size)
    paintfield(stdscr, field, size, colors, False)

    r, c = 0, 0
    nr, nc = 0, 0
    paintcell(stdscr, field[0][0], colors, True, False)

    while True:
        userkey = stdscr.getch()

        # 17 is ESC, 113 is q
        if userkey in [27, 113]:
            break;

        if userkey == curses.KEY_RIGHT:
            if c < size[1] - 1:
                nc = c + 1
        elif userkey == curses.KEY_LEFT:
            if c > 0:
                nc = c - 1
        elif userkey == curses.KEY_DOWN:
            if r < size[1] - 1:
                nr = r + 1
        elif userkey == curses.KEY_UP:
            if r > 0:
                nr = r - 1

        if nr == r and nc == c:
            # nothing changed!
            continue
        else:
            paintcell(stdscr, field[r][c], colors, False, False)
            paintcell(stdscr, field[nr][nc], colors, True, False)
            r, c = nr, nc

curses.wrapper(square)
