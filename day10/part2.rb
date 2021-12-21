require "./part1"

SCORES = { "(" => 1, "[" => 2, "{" => 3, "<" => 4 }

def score(opening_chars_to_close)
  opening_chars_to_close.reduce(0) do |total, char|
    total * 5 + SCORES.fetch(char)
  end
end

if __FILE__ == $0
  lines = ARGF.each_line.map { |line| line.chomp.each_char.to_a }
  incomplete_scores = lines.map.with_index do |line, index|
    score(read_line(line, index + 1).reverse)
  rescue CorruptedLineError
    nil
  end.compact
  puts(incomplete_scores.sort[incomplete_scores.size / 2])
end
