import sys
sys.path.append('./lib_py')

from human import Human
from bot import Bot

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
  print("playing {} games with '{}' strategy".format(number_of_games, strategy))
  tiles = []
  for i in range(int(number_of_games)):
    tiles.append(player.play())
  highest_tile = max(list(map(lambda x: x[0], tiles)))
  # will highest tile and highest score always be the same?
  score = max(list(map(lambda x: x[1], tiles)))
print("score = {} | highest tile {}".format(score, highest_tile))

