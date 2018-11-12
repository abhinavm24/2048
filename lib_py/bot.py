from game import Game, grouper
import random
import operator
import itertools
import math

def dedupe(my_list):
  # remove elements where the index of the first match is not the index of the item
  # in other words, remove subsequent occurrences of a list item
  return map(lambda tup: tup[1], filter(lambda tup: tup[0] == my_list.index(tup[1]), enumerate(my_list)))


class Bot:
  def __init__(self, strategy='highest_move'):
    self.directions = ['up', 'down', 'left', 'right']
    self.preferred_directions = ['up', 'left', 'right']
    self.strategies = {
      'random': self.strategy_random,
      'alex': self.strategy_alex,
      'highest_move': self.strategy_max_move_score,
      'forward_3': self.strategy_look_forward_3,
      'forward_3_pref': self.strategy_look_forward_3_preferred,
      'forward_5': self.strategy_look_forward_5,
      'forward_5_pref': self.strategy_look_forward_5_preferred,
      'forward_3_product': self.strategy_look_forward_3_product,
      'forward_3_pref_prod': self.strategy_look_forward_3_preferred_product,
      'forward_5_pref_prod': self.strategy_look_forward_5_preferred_product,
      'forward_4_prod': self.strategy_look_forward_4_product
    }
    self.strategy = self.strategies[strategy]

  def play(self):
    self.game = Game()
    while not self.game.is_complete():
      self.move(self.get_next_move())
      # print(self.game.board)
    return {
      'highest_tile': self.game.highest_tile(),
      'score': self.game.score,
      'board': self.game.board
    }

  def display(self, board = None):
    board = board if not None else self.game.board
    for row in grouper(board, 4):
      print(' '.join(map(str, row)))

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
  # all strategies should return a member of self.directions (i.e. a string)
  def strategy_random(self):
    return random.choice(self.directions)

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
        if before_board == self.game.board
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
    if highest_value == 0 or self.game.move(sequence[0], fake = True) == self.game.board:
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