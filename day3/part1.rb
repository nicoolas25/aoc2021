ONE = "1"
ZERO = "0"

lines = ARGF.each_line.map(&:chomp).to_a
counts = Array.new(lines.first.size) { 0 }
lines.each do |line|
  line.each_char.with_index do |c, i|
    counts[i] += 1 if c == ONE
  end
end
majority = lines.size / 2
gamma = counts.map { |n| n >= majority ? ONE : ZERO }.join.to_i(2)
epsilon = counts.map { |n| n >= majority ? ZERO : ONE }.join.to_i(2)

puts gamma * epsilon
