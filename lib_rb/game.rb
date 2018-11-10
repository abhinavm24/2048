class Game
  attr_reader :board

  def initialize
    @board = generate
    # set 2 tiles to "2"
    while @board.reject { |n| n == 0 }.size < 2 do
      @board[rand(0...16)] = 2
    end
  end

  def generate
    [
      0, 0, 0, 0,
      0, 0, 0, 0,
      0, 0, 0, 0,
      0, 0, 0, 0
    ]
  end

  def complete?(array = @board)
    result = true
    %w[up down left right].each do |direction|
      if move(direction, fake: true) != array
        result = false
        break
      end
    end
  end

  def highest_tile
    @board.max
  end

  def group(type, array = @board)
    new_a = array.each_slice(4).to_a
    if type == 'columns'
      new_a = new_a.transpose
    end
    new_a
  end

  def ungroup(type, array = @board)
    new_a = array
    if type == 'columns'
      new_a = array.transpose
    end
    new_a.flatten
  end

  def update(new_board, fake = false)
    # only generate new piece if board is different
    if fake
      new_board
    elsif @board != new_board
      @board = new_board
      random_index = @board.each_with_index.find_all{|n,i| n == 0}.map{|n,i| i }.sample
      @board[random_index] = 2
      @board
    end
  end

  def move(direction, fake: false)
    case direction
    when 'up'
      lines = group 'columns'
      new_lines = lines.map(&method(:collapse_line))
      update ungroup('columns', new_lines), fake
    when 'down'
      lines = group('columns').map { |line| line.reverse }
      new_lines = lines.map(&method(:collapse_line))
      update ungroup('columns', new_lines.map { |line| line.reverse }), fake
    when 'left'
      lines = group 'rows'
      new_lines = lines.map(&method(:collapse_line))
      update ungroup('rows', new_lines), fake
    when 'right'
      lines = group('rows').map { |line| line.reverse }
      new_lines = lines.map(&method(:collapse_line))
      update ungroup('rows', new_lines.map { |line| line.reverse }), fake
    else
      puts 'invalid move'
    end
  end

  def collapse_line(line)
    # move non-zeros to front if needed
    line = sort_zeros(line)
    line = combine_adjacent(line)
    line = sort_zeros(line)
    line
  end

  def sort_zeros(line)
    line[0..-1].sort do |a,b|
      if a == 0 
        1
      elsif b == 0
        -1
      elsif a > 0 && b > 0
        0
      else
        0 
      end
    end
  end

  def combine_adjacent(line)
    new_line = line[0..-1]
    line.each_index do |i|
      # no need to check the last value
      if i == line.size - 1
        break
      end
      if new_line[i + 1] == new_line[i]
        new_line[i + 1] = 0
        new_line[i] *= 2
      end
    end
    new_line
  end
end