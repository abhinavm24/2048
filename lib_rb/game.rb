class Array
  def deep_copy
    new_a = []
    self.each{|e| new_a << e.dup}
    new_a
  end
  alias_method :read_only, :deep_copy
end

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
      new_lines = lines.map(&method(:collapse_lines))
      update ungroup('columns', new_lines), fake
    when 'down'
      lines = group('columns').map { |line| line.reverse }
      new_lines = lines.map(&method(:collapse_lines))
      update ungroup('columns', new_lines.map { |line| line.reverse }), fake
    when 'left'
      lines = group 'rows'
      new_lines = lines.map(&method(:collapse_lines))
      update ungroup('rows', new_lines), fake
    when 'right'
      lines = group('rows').map { |line| line.reverse }
      new_lines = lines.map(&method(:collapse_lines))
      update ungroup('rows', new_lines.map { |line| line.reverse }), fake
    else
      puts 'invalid move'
    end
  end

  def collapse_lines2(line)
    puts line.inspect
    new_line = [0,0,0,0]
    line.each_with_index do |n, j|
      prior_values = if (j-1 < 0) then [] else new_line.take(j-1) end
      if n == 0
        next
      elsif prior_values.include? n
        new_line[new_line.index(n)] = n * 2
      else
        new_line[j] = n
      end
    end
    # need to remove 0s, and push non-zeros to front, then add "0" tiles in right places
    new_line = new_line.reject { |n| n == 0}
    while new_line.size < 4
      new_line << 0
    end
    new_line
  end

  def collapse_lines(line)
    # move non-zeros to front if needed
    if do_any_zeros_exist_before_numbers(line)
      line = move_non_zeros_to_front(line)
    end

    # if adjacent numbers are equal, they must be combined
    if do_adjacent_equal_numbers_exist(line)
      line = combine_adjacent_equal_numbers(line)
      # in case combining numbers created zeros, move numbers again
      line = move_non_zeros_to_front(line)
    end

    line
  end

  def do_any_zeros_exist_before_numbers(line)
    line != move_non_zeros_to_front(line)
  end

  def move_non_zeros_to_front(line)
    line.deep_copy.sort do |a,b|
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

  def do_adjacent_equal_numbers_exist(line)
    line != combine_adjacent_equal_numbers(line.deep_copy)
  end

  def combine_adjacent_equal_numbers(line)
    new_line = line.deep_copy
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