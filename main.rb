$LOAD_PATH << File.expand_path('lib_rb')

require 'game'
require 'human'
require 'bot'

puts "what kind of player? (human or bot)"
player_type = gets
if player_type.strip == 'human'
  player = Human.new
  highest_tile = player.play
else
  player = Bot.new
  tiles = []
  1000.times do
    tiles << player.play
  end
  highest_tile = tiles.max
end
puts "highest tile #{highest_tile}"






# game = Game.new
# puts game.collapse_lines([2, 2, 2, 2]).inspect
# puts game.move_non_zeros_to_front([4, 4, 2, 0]).inspect





# tests.... can definitely be deleted


# def move_non_zeros_to_front(line)
#   line.sort do |a,b|
#     if a == 0 
#       1
#     elsif b == 0
#       -1
#     elsif a > 0 && b > 0
#       0
#     else
#       0 
#     end
#   end
# end

# a = [1, 2, 0, 4]
# puts a.inspect, move_non_zeros_to_front(a).inspect
# a = [0, 0, 0, 4]
# puts a.inspect, move_non_zeros_to_front(a).inspect
# a = [0, 2, 0, 4]
# puts a.inspect, move_non_zeros_to_front(a).inspect
# a = [1, 2, 3, 4]
# puts a.inspect, move_non_zeros_to_front(a).inspect
# a = [0, 0, 4, 2]
# puts a.inspect, move_non_zeros_to_front(a).inspect
# a = [2, 0, 0, 4]
# puts a.inspect, move_non_zeros_to_front(a).inspect
# a = [2, 0, 2, 0]
# puts a.inspect, move_non_zeros_to_front(a).inspect
