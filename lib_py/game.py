import random

class Game:
  def __init__(self):
    self.board = self.generate()
    while len(list(filter(lambda x: x != 0, self.board))) < 2:
      self.board[random.randint(0, len(self.board) - 1)] = 2

  def generate(self):
    return [
      0, 0, 0, 0,
      0, 0, 0, 0,
      0, 0, 0, 0,
      0, 0, 0, 0
    ]

  def is_complete(self, array=None):
    array = array if array is not None else self.board
    return False

  def highest_tile(self):
    return max(self.board)

  def group(self, row_column, array=None):
    array = array if array is not None else self.board
    return []

  def ungroup(self, row_column, array=None):
    array = array if array is not None else self.board
    return []

  def update(self, new_board, fake = False):
    return self.board

  def move(self, direction, fake = False):
    if direction == 'up':
      update()
    elif direction == 'down':
      update()
    elif direction == 'left':
      update()
    elif direction == 'right':
      update()
    else:
      print('invalid move')

  # move numbers to front
  # combine
  # combining might create more zeros, so move to front again
  def collapse_line(self, line):
    line = self.move_non_zeros_to_front(line)
    line = self.combine_adjacent_equal_numbers(line)
    line = self.move_non_zeros_to_front(line)
    return line

  # this is kind of ugly but I can't figure out how to sort things in a more nuanced way
  def move_non_zeros_to_front(self, line):
    new_line = []
    for x in line:
      if x != 0:
        new_line.append(x)
    while len(new_line) < 4:
      new_line.append(0)
    return new_line

  def combine_adjacent_equal_numbers(self, line):
    new_line = line[:]
    for i, x in enumerate(line):
      # no need to check the last value
      if i == len(line) - 1:
        break
      if new_line[i + 1] == new_line[i]:
        new_line[i + 1] = 0
        new_line[i] *= 2
    return new_line