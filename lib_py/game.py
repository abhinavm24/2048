import random
from itertools import zip_longest

# credit: https://stackoverflow.com/a/434411/3991555, slightly modified
def grouper(iterable, n, fillvalue=None):
  args = [iter(iterable)] * n
  return list(map(list, zip_longest(*args, fillvalue=fillvalue)))

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

  def group(self, grouping, array=None):
    array = array if array is not None else self.board
    # group into nested list of lists, 4 items each
    nested_array = grouper(array, 4)
    if grouping == 'columns':
      # transpose - credit: https://stackoverflow.com/a/6473724/3991555
      nested_array = list(map(list, zip(*nested_array)))
    return nested_array

  def ungroup(self, grouping, array=None):
    array = array if array is not None else self.board
    flat_array = array[:]
    # transpose
    if grouping == 'columns':
      flat_array = list(map(list, zip(*flat_array)))
    # flatten - credit: https://stackoverflow.com/a/952952/3991555
    flat_array = [item for sublist in flat_array for item in sublist]
    return flat_array

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