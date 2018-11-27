$LOAD_PATH << File.expand_path('lib')

require 'game'

game = Game.new

puts "collapse_line"

raise game.collapse_line([0, 2, 2, 0]) unless [4, 0, 0, 0] == game.collapse_line([0, 2, 2, 0])
raise game.collapse_line([2, 2, 2, 2]) unless [4, 4, 0, 0] == game.collapse_line([2, 2, 2, 2])
raise game.collapse_line([0, 0, 2, 0]) unless [2, 0, 0, 0] == game.collapse_line([0, 0, 2, 0])
raise game.collapse_line([4, 2, 2, 0]) unless [4, 4, 0, 0] == game.collapse_line([4, 2, 2, 0])
raise game.collapse_line([4, 0, 2, 2]) unless [4, 4, 0, 0] == game.collapse_line([4, 0, 2, 2])
raise game.collapse_line([4, 0, 2, 2]) unless [4, 4, 0, 0] == game.collapse_line([4, 0, 2, 2])
raise game.collapse_line([0, 0, 4, 4]) unless [8, 0, 0, 0] == game.collapse_line([0, 0, 4, 4])
raise game.collapse_line([0, 4, 4, 4]) unless [8, 4, 0, 0] == game.collapse_line([0, 4, 4, 4])

puts "group columns"

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
raise game.group('columns', original) unless expected_columns == game.group('columns', original)

puts "group rows"

expected_rows = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12],
  [13, 14, 15, 16]
]
raise game.group('rows', original) unless expected_rows == game.group('rows', original)


