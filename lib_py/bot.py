from game import Game
import random
import operator

class Bot:
  def __init__(self, strategy='highest_move'):
    self.moves = ['up', 'down', 'left', 'right']
    self.strategies = {
      'random': self.strategy_random,
      'alex': self.strategy_alex,
      'highest_move': self.strategy_max_move_score
    }
    self.strategy = self.strategies[strategy]

  def play(self):
    self.game = Game()
    while not self.game.is_complete():
      self.move(self.get_next_move())
    return (self.game.highest_tile(), self.game.score_total)

  def set_strategy(self, strategy):
    if strategy != '' and strategy in self.strategies:
      self.strategy = self.strategies[strategy]

  def list_strategies(self):
    return "\n".join([key for key, value in self.strategies.items()])

  def move(self, direction):
    self.game.move(direction)
    # print(direction)

  # just change the strategy to change how the bot plays
  def get_next_move(self):
    return self.strategy()

  # define strategies
  # all strategies should return a member of self.moves (i.e. a string)
  def strategy_random(self):
    return random.choice(self.moves)

  def strategy_alex(self):
    """go up. if not up, go left. if not left, go right. never go down"""
    # slight modification: sometimes you have to go down...
    if self.game.move('up', fake = True) != self.game.board:
      return 'up'
    elif self.game.move('left', fake = True) != self.game.board:
      return 'left'
    elif self.game.move('right', fake = True) != self.game.board:
      return 'right'
    else:
      return 'down'

  def strategy_max_move_score(self):
    results = {}
    for direction in self.moves:
      self.game.move(direction, fake = True)
      results[direction] = self.game.score_move
    # return highest key in dictionary - credit: https://stackoverflow.com/a/268285/3991555
    highest_direction = max(results.items(), key=operator.itemgetter(1))[0]
    highest_value = results[highest_direction]
    if highest_value == 0:
      highest_direction = self.strategy_alex()
    return highest_direction

