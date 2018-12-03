import random

class Strategy:
  def __init__(self, game, directions = ['up', 'left', 'right', 'down']):
    self.game = game
    self.directions = directions

  def get_next_move(self):
    return random.choice(self.directions)

  def should_move_back(self):
    return True or False

  # the strategy here is to imitate the way a human might play
  # this allows the bot to play through several potential futures on each turn
  # and pick the one that is most profitable.
  # The way this is implemented is sort of cheating but I think it's a valid
  # approximation of the way a human might play
  def predict_future_plays(self, sequences):
    results = []
    for sequence in sequences:
      self.game.save()
      result = { 'sequence': sequence, 'direction': sequence[0], 'score': 0 }
      for direction in sequence:
        before_board = self.game.board[:]
        self.game.move(direction)
        # if any move results in no change, then break
        if before_board == self.game.board:
          break
      result['score'] = self.game.score
      results.append(result)
      self.game.reset()
    highest = max(results, key=operator.itemgetter('score'))
    highest_direction = highest['direction']
    highest_value = highest['score']
    # fallback if
    #   no move will score
    #   moving in the best "long term" way does not result in a change
    if highest_value == 0 or self.game.move(highest_direction, fake = True) == self.game.board:
      highest_direction = self.strategy_alex()
    return highest_direction



class Alex(Strategy):
  def __init__(self, game, directions):
    super().__init__(game, directions)
    self.game = game

  def get_next_move(self):
    """go up. if not up, go left. if not left, go right. never go down"""
    # slight modification: sometimes you have to go down...
    if self.game.move('up', fake = True) != self.game.board:
      print(self.game.move('up', fake = True), self.game.board)
      return 'up'
    elif self.game.move('left', fake = True) != self.game.board:
      return 'left'
    elif self.game.move('right', fake = True) != self.game.board:
      return 'right'
    else:
      return 'down'
