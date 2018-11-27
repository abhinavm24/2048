import sys
sys.path.append('./lib')

from functools import partial

from game import Game, compose
from bot import dedupe

game = Game()

assert True == True, 'sanity check'

print("collapse_line")

assert [4, 0, 0, 0] == game.collapse_line([0, 2, 2, 0]), game.collapse_line([0, 2, 2, 0])
assert [4, 4, 0, 0] == game.collapse_line([2, 2, 2, 2]), game.collapse_line([2, 2, 2, 2])
assert [2, 0, 0, 0] == game.collapse_line([0, 0, 2, 0]), game.collapse_line([0, 0, 2, 0])
assert [4, 4, 0, 0] == game.collapse_line([4, 2, 2, 0]), game.collapse_line([4, 2, 2, 0])
assert [4, 4, 0, 0] == game.collapse_line([4, 0, 2, 2]), game.collapse_line([4, 0, 2, 2])
assert [4, 4, 0, 0] == game.collapse_line([4, 0, 2, 2]), game.collapse_line([4, 0, 2, 2])
assert [8, 0, 0, 0] == game.collapse_line([0, 0, 4, 4]), game.collapse_line([0, 0, 4, 4])
assert [8, 4, 0, 0] == game.collapse_line([0, 4, 4, 4]), game.collapse_line([0, 4, 4, 4])

print("group columns")

original = [
  1, 2, 3, 4,
  5, 6, 7, 8,
  9, 10, 11, 12,
  13, 14, 15, 16
]
expected_columns = [
  [1, 5, 9, 13],
  [2, 6, 10, 14],
  [3, 7, 11, 15],
  [4, 8, 12, 16]
]
assert expected_columns == game.group('columns', original), game.group('columns', original)

print("group rows")

expected_rows = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12],
  [13, 14, 15, 16]
]
assert expected_rows == game.group('rows', original), game.group('rows', original)


print("compose")

f = lambda x: x * 2
g = lambda x, y, z: [x, y, z]
z = compose(f, g)
assert [1, 2, 3, 1, 2, 3] == z(1, 2, 3), z(1, 2, 3)

f1 = lambda x: x * 2
f2 = lambda l: list(map(lambda x: x * 2, l))
f3 = lambda x, y, z: [x, y, z]
z = compose(f1, f2, f3)
assert [2, 4, 6, 2, 4, 6] == z(1, 2, 3), z(1, 2, 3)


print("partial")

f = lambda x: x * 2
g = lambda x, y, z: [x, y, z]
z = compose(f, partial(g, 1, 2))
assert [1, 2, 3, 1, 2, 3] == z(3), z(3)


print("dedupe")

assert [(1, 2), (2, 3), (3, 4)] == list(dedupe([(1, 2), (2, 3), (3, 4), (1, 2), (2, 3), (3, 4)])), dedupe([(1, 2), (2, 3), (3, 4), (1, 2), (2, 3), (3, 4)])


print('is_complete')
board = [64, 2048, 256, 128, 32, 256, 32, 8, 8, 16, 4, 0, 4, 2, 0, 0]
game.board = board
assert game.is_complete(board) != True, game.board
assert game.move('up', fake = True) == game.board, "{}, {}".format(game.move('up', fake = True), game.board)
assert game.move('down', fake = True) != game.board, "{}, {}".format(game.move('down', fake = True), game.board)
assert game.move('left', fake = True) == game.board, "{}, {}".format(game.move('left', fake = True), game.board)
assert game.move('right', fake = True) != game.board, "{}, {}".format(game.move('right', fake = True), game.board)