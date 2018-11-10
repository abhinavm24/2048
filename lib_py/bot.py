from game import Game
import random

class Bot:
  def __init__(self):
    self.moves = ['up', 'down', 'left', 'right']
    self.strategies = {
      'random': self.strategy_random,
      'alex': self.strategy_alex
    }

  def play(self):
    self.game = Game()
    while not self.game.is_complete():
      self.move(self.get_next_move())
    return self.game.highest_tile()

  def move(self, direction):
    self.game.move(direction)
    # print(direction)

  # just change the strategy to change how the bot plays
  def get_next_move(self):
    return self.strategies['alex']()

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

