require "./part1"

if __FILE__ == $0
  total = 0
  ARGF.each_line.map do |line|
    samples, digits = line.chomp.split(" | ").map(&:split)
    ssd = SevenSegmentDisplay.new(samples)
    total += digits.map { |digit| ssd.translate_digit(digit).to_s }.join.to_i
  end
  puts(total)
end
