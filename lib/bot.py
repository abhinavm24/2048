from game import Game
from util import grouper, compose, transpose, flatten, display_board, dedupe
from strategy import *

class Bot:
  def __init__(self, verbose = 'quiet'):
    self.directions = ['up', 'down', 'left', 'right']
    self.preferred_directions = ['up', 'left', 'right']
    self.strategies = [
      {'name': 'random', 'class': Strategy},
      {'name': 'alex', 'class': Alex},
      {'name': 'highest move', 'class': MoveMaxScore},

      {'name': 'forward permutation 3', 'class': ForwardPermutation3},
      {'name': 'forward permutation 3 [preferred directions]', 'class': ForwardPermutation3Preferred},
      {'name': 'forward permutation 4', 'class': ForwardPermutation4},
      {'name': 'forward permutation 4 [preferred directions]', 'class': ForwardPermutation4Preferred},
      {'name': 'forward permutation 5', 'class': ForwardPermutation5},
      {'name': 'forward permutation 5 [preferred directions]', 'class': ForwardPermutation5Preferred},

      {'name': 'forward product 3', 'class': ForwardProduct3},
      {'name': 'forward product 3 [preferred directions]', 'class': ForwardProduct3Preferred},
      {'name': 'forward product 4', 'class': ForwardProduct4},
      {'name': 'forward product 4 [preferred directions]', 'class': ForwardProduct4Preferred},
      {'name': 'forward product 5', 'class': ForwardProduct5},
      {'name': 'forward product 5 [preferred directions]', 'class': ForwardProduct5Preferred},

      {'name': '[WIP] snake', 'class': Snake}
    ]
    self.default_strategy = 2
    self.game = Game()
    self.verbose = verbose == 'verbose'

  def play(self):
    self.game = Game()
    while not self.game.is_complete():
      next_move = self.strategy.get_next_move(self.game)
      if (self.verbose):
        self.display(self.game.board)
        print("Next move: {}".format(next_move))
        print("Highest tile on board: {}".format(self.game.highest_tile()))
        print("Current score: {}".format(self.game.score))
      self.move(next_move)
      if self.strategy.should_move_back(self.game):
        if (self.verbose):
          print("Moving back, previous move sucked")
        self.move('back')
    return {
      'highest_tile': self.game.highest_tile(),
      'score': self.game.score,
      'board': self.game.board
    }

  def display(self, board = None):
    board = board if not None else self.game.board
    return display_board(board)

  def set_strategy(self, strategy):
    try:
      strategy = int(strategy)
      assert strategy >= 0 and strategy < len(self.strategies)
    except:
      strategy = self.default_strategy
    self.strategy = self.strategies[strategy]['class'](self.directions)
    return self.strategies[strategy]['name']

  def list_strategies(self):
    return "\n".join(["{}: {} {}".format(i, strategy['name'], '(DEFAULT)' if i == self.default_strategy else '') for i, strategy in enumerate(self.strategies)])

  def move(self, direction):
    self.game.move(direction)
