class Line
  attr_reader :parse_error_on

  OPENING_TO_CLOSING_CHAR = {
    "(" => ")",
    "[" => "]",
    "<" => ">",
    "{" => "}",
  }

  def initialize(content)
    parse(content)
  end

  def corrupted?
    !!@parse_error_on
  end

  private

  def parse(content)
    @closing_chars = []
    content.each_char do |char|
      if closing_char = OPENING_TO_CLOSING_CHAR[char]
        @closing_chars.unshift(closing_char)
      else
        next_closing_char = @closing_chars.shift
        if next_closing_char != char
          @parse_error_on = char
          break
        end
      end
    end
  end
end

if __FILE__ == $0
  scores = { ")" => 3, "]" => 57, "}" => 1197, ">" => 25137 }
  lines = ARGF.each_line.map { |line| Line.new(line.chomp) }
  puts(lines.sum { |l| l.corrupted? ? scores[l.parse_error_on] : 0 })
end
