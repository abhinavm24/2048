from itertools import zip_longest
from functools import reduce, partial

# credit: https://stackoverflow.com/a/434411/3991555, slightly modified
def grouper(iterable, n, fillvalue=None):
  args = [iter(iterable)] * n
  return list(map(list, zip_longest(*args, fillvalue=fillvalue)))

# build up some functional elements
# inspired by https://docs.python.org/3.1/howto/functional.html
compose2 = lambda f, g: lambda *x: f(g(*x))
compose = lambda *x: reduce(compose2, list(x))
list_map = compose(list, map)
map_to_list = compose(list, partial(map, list))
# transpose - credit: https://stackoverflow.com/a/6473724/3991555
transpose = compose(map_to_list, zip)
# flatten - credit: https://stackoverflow.com/a/952952/3991555
flatten = lambda nested_array: [item for sublist in nested_array for item in sublist]

def right_pad(min_digits, number):
  stringified = str(number)
  if len(stringified) < min_digits:
    return stringified + (' ' * (min_digits - len(stringified)))
  else:
    return stringified

def display_board(board):
  pad = partial(right_pad, 4)
  for row in grouper(board, 4):
    print(' '.join(map(pad, row)))
    print()

def dedupe(my_list):
  # remove elements where the index of the first match is not the index of the item
  # in other words, remove subsequent occurrences of a list item
  return map(lambda tup: tup[1], filter(lambda tup: tup[0] == my_list.index(tup[1]), enumerate(my_list)))
