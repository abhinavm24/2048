import sys
sys.path.append('./lib_py')

from human import Human
from bot import Bot
import operator

player_type = input("are you human? (y/n): ")
if player_type.strip() == 'y':
  player = Human()
  (highest_tile, score) = player.play()
else:
  player = Bot()
  number_of_games = input("how many games would you like to play? (default: 100) ")
  try:
    int(number_of_games)
  except:
    number_of_games = 100
  strategy = input("what strategy would you like to use? (default: highest_move) \noptions: \n{} \n".format(player.list_strategies()))
  if strategy == '':
    strategy = 'highest_move'
  player.set_strategy(strategy)
  print("playing {} games with '{}' strategy".format(number_of_games, strategy))
  tiles = []
  for i in range(int(number_of_games)):
    print('playing game {}'.format(i + 1))
    tiles.append(player.play())
  highest = max(tiles, key=operator.itemgetter('score'))
  highest_tile = highest['highest_tile']
  score = highest['score']
  board = highest['board']
  player.display(board)
print("score = {} | highest tile {}".format(score, highest_tile))

