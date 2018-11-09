import sys
sys.path.append('./lib_py')

from game import Game

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