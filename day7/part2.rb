require "./part1"

def cost(n, numbers)
  numbers.sum do |x|
    m = (x - n).abs
    m * (m+1) / 2
  end
end

if __FILE__ == $0
  numbers = ARGF.each_line.first.chomp.split(",").map(&:to_i).sort
  puts(reduce_cost(numbers.sum / numbers.length, numbers))
end
