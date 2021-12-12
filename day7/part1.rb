def cost(n, numbers)
  numbers.sum { |x| (x - n).abs }
end

def reduce_cost(n, sorted_numbers)
  cost = cost(n, sorted_numbers)
  left_cost = cost(n - 1, sorted_numbers)
  right_cost = cost(n + 1, sorted_numbers)
  if left_cost > cost && right_cost > cost
    cost
  elsif left_cost < cost
    reduce_cost(n - 1, sorted_numbers)
  else
    reduce_cost(n + 1, sorted_numbers)
  end
end

if __FILE__ == $0
  numbers = ARGF.each_line.first.chomp.split(",").map(&:to_i).sort
  puts(reduce_cost(numbers.sum / numbers.length, numbers))
end
