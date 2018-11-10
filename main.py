import sys
sys.path.append('./lib_py')

from human import Human
from bot import Bot

player_type = input("are you human? (y/n): ")
if player_type.strip() == 'y':
  player = Human()
  highest_tile = player.play()
else:
  player = Bot()
  tiles = []
  for i in range(100000):
    tiles.append(player.play())
  highest_tile = max(tiles)
print("highest tile {highest}".format(highest = highest_tile))

