import random
import itertools
import operator
import math


# To make a new strategy, simply subclass Strategy
#
# get_next_move() method must return the direction to move next
#
# should_move_back(), if overridden, should return a boolean iff the resulting move should be reverted
# (keep in mind you can only move back once. You may want to track the number of "back"s internally so you don't 
# enter an infinite loop of trying to go back)

class Strategy:
  def __init__(self, directions = ['up', 'left', 'right', 'down']):
    self.directions = directions

  # return a direction
  def get_next_move(self, game):
    return random.choice(self.directions)

  # return a boolean
  # override if you want to analyze the board and conditionally move back
  def should_move_back(self, game):
    return False

  # the strategy here is to imitate the way a human might play
  # this allows the bot to play through several potential futures on each turn
  # and pick the one that is most profitable.
  # The way this is implemented is sort of cheating but I think it's a valid
  # approximation of the way a human might play
  def predict_future_plays(self, game, sequences):
    results = []
    for sequence in sequences:
      game.save()
      result = { 'sequence': sequence, 'direction': sequence[0], 'score': 0 }
      for direction in sequence:
        before_board = game.board[:]
        game.move(direction)
        # if any move results in no change, then break
        if before_board == game.board:
          break
      result['score'] = game.score
      results.append(result)
      game.reset()
    highest = max(results, key=operator.itemgetter('score'))
    highest_direction = highest['direction']
    highest_value = highest['score']
    # fallback if
    #   no move will score
    #   moving in the best "long term" way does not result in a change
    if highest_value == 0 or game.move(highest_direction, fake = True) == game.board:
      highest_direction = self.fallback_move()
    return highest_direction

  def fallback_move(self, game):
    """go up. if not up, go left. if not left, go right. Only go down if absolutely necessary"""
    if game.move('up', fake = True) != game.board:
      return 'up'
    elif game.move('left', fake = True) != game.board:
      return 'left'
    elif game.move('right', fake = True) != game.board:
      return 'right'
    else:
      return 'down'


class Alex(Strategy):
  def get_next_move(self, game):
    return super().fallback_move(game)


class MoveMaxScore(Strategy):
  def get_next_move(self, game):
    results = []
    for direction in self.directions:
      game.move(direction, fake = True)
      results.append({'direction': direction, 'score': game.score_move})
    # return highest key in dictionary - credit: https://stackoverflow.com/a/268285/3991555
    highest = max(results, key=operator.itemgetter('score'))
    highest_direction = highest['direction']
    highest_value = highest['score']
    # fallback if
    #   no move will score
    if highest_value == 0:
      highest_direction = self.fallback_move()
    return highest_direction


# use permutations to get possible move sequences
class ForwardPermutation(Strategy):
  def __init__(self, directions, number_of_future_moves = 3):
    super().__init__(directions)
    self.number_of_future_moves = number_of_future_moves

  def get_next_move(self, game):
    sequences = itertools.permutations(self.directions, self.number_of_future_moves)
    return self.predict_future_plays(game, sequences)

class ForwardPermutation3(ForwardPermutation):
  def __init__(self, directions):
    super().__init__(directions, 3)

class ForwardPermutation3Preferred(ForwardPermutation):
  def __init__(self, directions):
    super().__init__(directions[0:3], 3)

class ForwardPermutation4(ForwardPermutation):
  def __init__(self, directions):
    super().__init__(directions, 4)

class ForwardPermutation4Preferred(ForwardPermutation):
  def __init__(self, directions):
    super().__init__(directions[0:3], 4)

class ForwardPermutation5(ForwardPermutation):
  def __init__(self, directions):
    super().__init__(directions, 5)

class ForwardPermutation5Preferred(ForwardPermutation):
  def __init__(self, directions):
    super().__init__(directions[0:3], 5)



# use cartesion product instead of permutations to get possible move sequences
class ForwardProduct(Strategy):
  def __init__(self, directions, number_of_future_moves = 3):
    super().__init__(directions)
    self.number_of_future_moves = number_of_future_moves

  def get_next_move(self, game):
    sequences = itertools.product(self.directions, repeat=self.number_of_future_moves)
    return self.predict_future_plays(game, sequences)

class ForwardProduct3(ForwardProduct):
  def __init__(self, directions):
    super().__init__(directions, 3)

class ForwardProduct3Preferred(ForwardProduct):
  def __init__(self, directions):
    super().__init__(directions[0:3], 3)

class ForwardProduct4(ForwardProduct):
  def __init__(self, directions):
    super().__init__(directions, 4)

class ForwardProduct4Preferred(ForwardProduct):
  def __init__(self, directions):
    super().__init__(directions[0:3], 4)

class ForwardProduct5(ForwardProduct):
  def __init__(self, directions):
    super().__init__(directions, 5)

class ForwardProduct5Preferred(ForwardProduct):
  def __init__(self, directions):
    super().__init__(directions[0:3], 5)




class Snake(Strategy):
  def __init__(self, directions):
    super().__init__(directions[0:3])

  def get_next_move(self, game):
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
      for direction in self.directions:
        new_board = game.move(direction, fake = True)
        if new_board[n] > game.board[n]:
          return direction
    # if we haven't found any moves that increase the value of a piece in priority sequence,
    # then just default to the Alex strategy
    return self.fallback_move()




# I don't think this is very well conceived
class Snake2(Strategy):
  def get_next_move(self, game):
    """We define our priorites in a "snake" design, going from upper left (0,0) to bottom left (0,3)
    in an 'S' pattern, left to right, top to bottom
    The goal is to always maximize the tile number in the highest priority space possible"""
    # find the index in the board that corresponds to our next piece of interest
    # TODO: make this more complex, e.g. consider adjacent piece value
    target_index = self.find_highest_priority_nonzero_index()
    original_tile_value = game.board[target_index]
    # try each available move
    for direction in self.directions:
      new_board = game.move(direction, fake = True)
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
      enumerate(grouper(game.board, 4))
    )
