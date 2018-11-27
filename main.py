import sys
sys.path.append('./lib')

from human import Human
from bot import Bot
import operator

player_type = input("are you human? (y/n): ")
if player_type.strip() == 'y':
  player = Human()
  (highest_tile, score) = player.play()
else:
  player = Bot()

  # get number of games to play
  number_of_games = input("how many games would you like to play? (default: 100) ")
  try:
    int(number_of_games)
  except:
    number_of_games = 100

  # get strategy to play with
  strategy = input("what strategy would you like to use? (enter a number)\n{} \n".format(player.list_strategies()))
  strategy = player.set_strategy(strategy)
  
  # play number of games with desired strategy
  print("playing {} games with '{}' strategy".format(number_of_games, strategy))
  tiles = []
  for i in range(int(number_of_games)):
    print('playing game {}'.format(i + 1))
    tiles.append(player.play())

  # get highest score from all the games played
  highest = max(tiles, key=operator.itemgetter('score'))
  highest_tile = highest['highest_tile']
  score = highest['score']
  board = highest['board']
  player.display(board)
print("score = {} | highest tile {}".format(score, highest_tile))

