require 'game'

class Bot
  def initialize(verbose = false)
    @verbose = verbose
    @game = Game.new
    @moves = %w[up down left right]
    display if @verbose
  end

  def display
    puts @game.board[0...4].join(' ')
    puts @game.board[4...8].join(' ')
    puts @game.board[8...12].join(' ')
    puts @game.board[12...16].join(' ')
    puts
  end

  # returns one of @moves
  def get_next_move
    # define strategy
    if @game.complete?
      'down'
    else
      (@moves - ['down']).sample
    end
  end

  def move
    direction = get_next_move
    @game.move direction
    if @verbose
      # system "clear" or system "cls"
      puts direction
      display
    end
  end

  def play 
    while !@game.complete? do
      move
    end

    @game.highest_tile
  end
end