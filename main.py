import sys
sys.path.append('./lib_py')

from human import Human
from bot import Bot

player_type = input("what kind of player? (human or bot): ")
print(repr(player_type))
print(repr(player_type.strip()))
if player_type.strip() == 'human':
  player = Human()
  highest_tile = player.play()
else:
  player = Bot()
  tiles = []
  for i in range(1000):
    tiles.append(player.play)
  highest_tile = tiles.max
print("highest tile {highest}".format(highest = highest_tile))

