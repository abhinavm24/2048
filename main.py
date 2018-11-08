import sys
sys.path.append('./lib_py')

from human import Human
from bot import Bot

player_type = input("what kind of player? (human or bot): ")
if player_type.strip == 'human'
  player = Human()
  highest_tile = player.play
else
  player = Bot()
  tiles = []
  1000.times do
    tiles.append(player.play)
  end
  highest_tile = tiles.max
end
print("highest tile {highest}".format(highest = highest_tile))

