from game import Game
import random

class Bot:
  def __init__(self):
    self.game = Game()
    self.moves = ['up', 'down', 'left', 'right']

  def play(self):
    while not self.game.is_complete():
      self.move(self.get_next_move())
    return self.game.highest_tile()

  def move(self, direction):
    self.game.move(direction)
    # print(direction)

  # for now, just random
  def get_next_move(self):
    return random.choice(self.moves)
