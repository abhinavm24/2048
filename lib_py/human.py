from game import Game

class Human:
  def __init__(self):
    self.game = Game()
    self.moves = {
      "\e[A\n": 'up',
      "\e[C\n": 'right',
      "\e[D\n": 'left',
      "\e[B\n": 'down'
    }

  def play():
    print('playing')
    direction_trimmed = ''
    while !(direction_trimmed == "q" or direction_trimmed == "quit" or direction_trimmed == 'exit' or self.game.is_complete())
      direction = input()
      direction_trimmed = direction.replace(r"\s", "")
      move(direction)

    return self.game.highest_tile()

  def display():
    print(self.game.board)

  def move(direction):
    game.move(moves[direction])
    print(moves[direction])
    display

