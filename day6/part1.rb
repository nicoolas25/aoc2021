numbers = ARGF.each_line.first.chomp.split(",").map(&:to_i)

80.times do
  new_fish_count = 0
  numbers.map! do |n|
    if n == 0
      new_fish_count += 1
      6
    else
      n - 1
    end
  end
  numbers.concat([8] * new_fish_count)
end

puts(numbers.size)
