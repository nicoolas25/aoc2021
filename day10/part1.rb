OPENING_TO_CLOSING_CHAR = {
  "(" => ")",
  "[" => "]",
  "<" => ">",
  "{" => "}",
}

class CorruptedLineError < StandardError
  attr_reader :line_nr
  attr_reader :column_nr
  attr_reader :expected
  attr_reader :found

  def initialize(line_nr, column_nr, expected, found)
    @line_nr = line_nr
    @column_nr = column_nr
    @expected = expected
    @found = found
    super("Corrupted line @#{line_nr}:#{column_nr}: found: #{found}, expected: #{expected}")
  end
end

def read_line(line, line_nr)
  opening_chars_stack = []
  line.each.with_index do |char, index|
    if OPENING_TO_CLOSING_CHAR.has_key?(char)
      opening_chars_stack << char
    else
      latest_opening_char = opening_chars_stack.pop
      expected_char = OPENING_TO_CLOSING_CHAR.fetch(latest_opening_char)
      if expected_char != char
        raise CorruptedLineError.new(line_nr, index + 1, expected_char, char)
      end
    end
  end
  opening_chars_stack
end

if __FILE__ == $0
  scores = { ")" => 3, "]" => 57, "}" => 1197, ">" => 25137 }
  lines = ARGF.each_line.map { |line| line.chomp.each_char.to_a }
  errors = lines.map.with_index do |line, index|
    read_line(line, index + 1)
    nil
  rescue CorruptedLineError => cle
    scores.fetch(cle.found)
  end.compact
  puts(errors.sum)
end
