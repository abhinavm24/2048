require 'game'

class Human
  def initialize
    @game = Game.new
    @moves = {
      "\e[A\n" => 'up',
      "\e[C\n" => 'right',
      "\e[D\n" => 'left',
      "\e[B\n" => 'down'
    }
    @moves.default = 'invalid move'
    display
  end

  def display
    puts @game.board[0...4].join(' ')
    puts @game.board[4...8].join(' ')
    puts @game.board[8...12].join(' ')
    puts @game.board[12...16].join(' ')
  end

  def move(direction)
    @game.move @moves[direction]
    # system "clear" or system "cls"
    display
  end

  def play 
    direction = ''
    while !(direction.strip == "q" || direction.strip == "quit" || direction.strip == 'exit' || @game.complete?) do
      direction = gets
      move direction
    end

    @game.highest_tile
  end
end