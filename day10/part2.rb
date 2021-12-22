require "./part1"

# Reopen the class to add an accessor for remaining closing_chars
class Line
  attr_reader :closing_chars
end

if __FILE__ == $0
  scores = { ")" => 1, "]" => 2, "}" => 3, ">" => 4 }
  incomplete_scores = ARGF.each_line
    .map { |line| Line.new(line.chomp) }
    .reject { |line| line.corrupted? || line.closing_chars.empty? }
    .map do |line|
      line.closing_chars.reduce(0) do |total, char|
        total * 5 + scores.fetch(char)
      end
    end
  puts(incomplete_scores.sort[incomplete_scores.size / 2])
end
