def count(days, number, cache = {})
  cache[[days, number]] ||= begin
    if days <= number
      1
    else
      count(days - number, 7, cache) + count(days - number, 9, cache)
    end
  end
end

numbers = ARGF.each_line.first.chomp.split(",").map(&:to_i)
puts(numbers.sum { |number| count(256, number) })
