from game import Game, grouper
from util import display_board
from functools import partial

class Human:
  def __init__(self):
    self.game = Game()
    self.directions = {
      "\x1b[A": 'up',
      "\x1b[C": 'right',
      "\x1b[D": 'left',
      "\x1b[B": 'down'
    }
    self.display()

  def play(self):
    print('playing')
    direction_trimmed = ''
    while not (direction_trimmed == "q" or direction_trimmed == "quit" or direction_trimmed == 'exit' or self.game.is_complete()):
      direction = input()
      direction_trimmed = direction.replace(r"\s", "")
      self.move(direction)

    return (self.game.highest_tile(), self.game.score)

  def display(self):
    return display_board(self.game.board)

  def move(self, direction):
    human_readable_move = self.get_direction(direction)
    self.game.move(human_readable_move)
    print(human_readable_move)
    self.display()

  def get_direction(self, direction):
    try:
      return self.directions[direction]
    except:
      return 'invalid move'

