from game import Game
from util import grouper, compose, transpose, flatten, display_board, dedupe
import random
import operator
import itertools
import math
from strategy import *

class Bot:
  def __init__(self, verbose = 'quiet'):
    self.directions = ['up', 'down', 'left', 'right']
    self.preferred_directions = ['up', 'left', 'right']
    self.strategies = [
      {'name': 'random', 'func': Strategy},
      {'name': 'alex', 'func': Alex},
      {'name': 'highest_move', 'func': self.strategy_max_move_score},
      {'name': 'forward_3', 'func': self.strategy_look_forward_3},
      {'name': 'forward_3_pref', 'func': self.strategy_look_forward_3_preferred},
      {'name': 'forward_5', 'func': self.strategy_look_forward_5},
      {'name': 'forward_5_pref', 'func': self.strategy_look_forward_5_preferred},
      {'name': 'forward_3_product', 'func': self.strategy_look_forward_3_product},
      {'name': 'forward_3_pref_prod', 'func': self.strategy_look_forward_3_preferred_product},
      {'name': 'forward_5_pref_prod', 'func': self.strategy_look_forward_5_preferred_product},
      {'name': 'forward_4_prod', 'func': self.strategy_look_forward_4_product},
      {'name': '[WIP] snake', 'func': self.strategy_snake}
    ]
    self.default_strategy = 2
    self.game = Game()
    self.verbose = verbose == 'verbose'

  def play(self):
    self.game = Game()
    while not self.game.is_complete():
      
      next_move = self.strategy.get_next_move()
      if (self.verbose):
        self.display(self.game.board)
        self.display(self.strategy.game.board)
        print(next_move, self.game.highest_tile(), self.game.score)
      self.move(next_move)
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
    self.strategy = self.strategies[strategy]['func'](self.game, self.directions)
    return self.strategies[strategy]['name']

  def list_strategies(self):
    return "\n".join(["{}: {} {}".format(i, strategy['name'], '(default)' if i == self.default_strategy else '') for i, strategy in enumerate(self.strategies)])

  def move(self, direction):
    self.game.move(direction)

  # define strategies
  # all strategies should return a member of self.directions (i.e. a string)

  def strategy_max_move_score(self):
    results = []
    for direction in self.directions:
      self.game.move(direction, fake = True)
      results.append({'direction': direction, 'score': self.game.score_move})
    # return highest key in dictionary - credit: https://stackoverflow.com/a/268285/3991555
    highest = max(results, key=operator.itemgetter('score'))
    highest_direction = highest['direction']
    highest_value = highest['score']
    # fallback if
    #   no move will score
    if highest_value == 0:
      highest_direction = self.strategy_alex()
    return highest_direction

  def strategy_look_forward_3(self):
    # create permutations to try
    sequences = itertools.permutations(self.directions, 3)
    return self.predict_future_plays(sequences)

  def strategy_look_forward_3_preferred(self):
    sequences = itertools.permutations(self.preferred_directions, 3)
    return self.predict_future_plays(sequences)

  def strategy_look_forward_5(self):
    # have to multiple by 2 so there are enough elements to create the larger permutations
    sequences = itertools.permutations(self.directions * 2, 5)
    return self.predict_future_plays(dedupe(list(sequences)))

  def strategy_look_forward_5_preferred(self):
    sequences = itertools.permutations(self.preferred_directions * 2, 5)
    return self.predict_future_plays(dedupe(list(sequences)))

  def strategy_look_forward_3_product(self):
    # create cartesian products
    # these will repeat the same move many times, which is realistic since that is valid and sometimes preferable in the game
    sequences = itertools.product(self.directions, repeat=3)
    return self.predict_future_plays(sequences)

  def strategy_look_forward_3_preferred_product(self):
    sequences = itertools.product(self.preferred_directions, repeat=3)
    return self.predict_future_plays(sequences)

  def strategy_look_forward_4_product(self):
    sequences = itertools.product(self.directions, repeat=4)
    return self.predict_future_plays(sequences)

  def strategy_look_forward_5_preferred_product(self):
    sequences = itertools.product(self.preferred_directions, repeat=5)
    return self.predict_future_plays(sequences)

  def strategy_snake(self):
    priority = [
      0,  1,  2,  3,
      7,  6,  5,  4,
      8,  9,  10, 11,
      15, 14, 13, 12
    ]
    # loop through all pieces in priority order
    for i, n in enumerate(priority):
      # try all available moves
      # if any increase the value, move to the next piece
      for direction in self.preferred_directions:
        new_board = self.game.move(direction, fake = True)
        if new_board[n] > self.game.board[n]:
          return direction
    # if we haven't found any moves that increase the value of a piece in priority sequence,
    # then just default to the Alex strategy
    return self.strategy_alex()






  def strategy_snake2(self):
    """We define our priorites in a "snake" design, going from upper left (0,0) to bottom left (0,3)
    in an 'S' pattern, left to right, top to bottom
    The goal is to always maximize the tile number in the highest priority space possible"""
    # find the index in the board that corresponds to our next piece of interest
    # TODO: make this more complex, e.g. consider adjacent piece value
    target_index = self.find_highest_priority_nonzero_index()
    original_tile_value = self.game.board[target_index]
    # try each available move
    for direction in self.preferred_directions:
      new_board = self.game.move(direction, fake = True)
      if new_board[target_index] <= original_tile_value:
        pass

  def find_highest_priority_nonzero_index(self):
    # maps the value in the "prioritized" board to its original index
    original_index_map = [
      0,  1,  2,  3,
      7,  6,  5,  4,
      8,  9,  10, 11,
      15, 14, 13, 12
    ]
    for i, n in enunmerate(self.prioritize_board()):
      if n == 0:
        return original_index_map[i]


  def prioritize_board(self):
    """ priority looks like this:
    [
      0,  1,  2,  3,
      7,  6,  5,  4,
      8,  9,  10, 11,
      15, 14, 13, 12
    ]
    """
    transform = compose(flatten, list, map)
    return transform(
      lambda tup: tup[1] if tup[0] % 2 == 0 else list(reversed(tup[1])),
      enumerate(grouper(self.game.board, 4))
    )
