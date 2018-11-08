import sys
sys.path.append('./lib_py')

from game import Game

game = Game()

assert True == True, 'sanity check'

assert [4, 0, 0, 0] == game.collapse_line([0, 2, 2, 0]), game.collapse_line([0, 2, 2, 0])

assert [4, 4, 0, 0] == game.collapse_line([2, 2, 2, 2]), game.collapse_line([2, 2, 2, 2])

assert [2, 0, 0, 0] == game.collapse_line([0, 0, 2, 0]), game.collapse_line([0, 0, 2, 0])

assert [4, 4, 0, 0] == game.collapse_line([4, 2, 2, 0]), game.collapse_line([4, 2, 2, 0])

assert [4, 4, 0, 0] == game.collapse_line([4, 0, 2, 2]), game.collapse_line([4, 0, 2, 2])

assert [4, 4, 0, 0] == game.collapse_line([4, 0, 2, 2]), game.collapse_line([4, 0, 2, 2])

assert [8, 0, 0, 0] == game.collapse_line([0, 0, 4, 4]), game.collapse_line([0, 0, 4, 4])

assert [8, 4, 0, 0] == game.collapse_line([0, 4, 4, 4]), game.collapse_line([0, 4, 4, 4])
