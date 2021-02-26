import curses
import math
import random

def initfield(center, size):

  # the field variable to store all cells.
  field = []

  # using row (r) and column (c) for index
  r, c = 0, 0
  # nested loop
  for y in range(center[0] - size[0] // 2, center[0] + size[0] // 2):
    # initialize each row.
    # repeat the size of column
    field.append([[0,0,0]] * size[1])
    for x in range(center[1] - size[1], center[1] + size[1], 2):
      field[r][c] = [y, x, 0]
      #stdscr.addstr(y, x, chr(9608))
      # done one column in a row.
      # increase the column index.
      c = c + 1
    # done one row. increase the row index.
    r = r + 1
    # reset column index to 0
    c = 0

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

def paintfield(stdscr, field, size):

    for r in range(0, size[0]):
        for c in range(0, size[1]):
            if field[r][c][2] == -1:
                stdscr.addstr(field[r][c][0], field[r][c][1], chr(10041))
            else:
                #stdscr.addstr(field[r][c][0], field[r][c][1], chr(9608))
                stdscr.addstr(field[r][c][0], field[r][c][1], str(field[r][c][2]))

def square(stdscr):

  curses.curs_set(0)

  sh, sw = stdscr.getmaxyx()
  center = [sh // 2, sw // 2]

  # row, column pair
  size = [20, 50]

  field = initfield(center, size)
  paintfield(stdscr, field, size)

  stdscr.getch()

curses.wrapper(square)
