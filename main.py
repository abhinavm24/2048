import sys
sys.path.append('./lib_py')

from human import Human
from bot import Bot

player_type = input("are you human? (y/n): ")
if player_type.strip() == 'y':
  player = Human()
  (highest_tile, score) = player.play()
else:
  player = Bot() # can pass a strategy here if desired
  tiles = []
  for i in range(1000):
    tiles.append(player.play())
  highest_tile = max(list(map(lambda x: x[0], tiles)))
  # will highest tile and highest score always be the same?
  score = max(list(map(lambda x: x[1], tiles)))
print("score = {} | highest tile {}".format(score, highest_tile))

