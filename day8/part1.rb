require "set"

REF_DIGIT_TO_WIRES = {
  0 => "abcefg",
  1 => "cf",
  2 => "acdeg",
  3 => "acdfg",
  4 => "bcdf",
  5 => "abdfg",
  6 => "abdefg",
  7 => "acf",
  8 => "abcdefg",
  9 => "abcdfg",
}
REF_WIRES_TO_DIGIT = REF_DIGIT_TO_WIRES.invert

class SevenSegmentDisplay
  def initialize(samples)
    @samples = samples
  end

  def translate_digit(wires)
    REF_WIRES_TO_DIGIT.fetch(wires.tr(translation_key, "abcdefg").each_char.sort.join)
  end

  private

  def translation_key
    @_translation_key ||= "abcdefg".each_char.to_a.permutation.find do |key|
      tr_key = key.join
      @samples.all? do |sample_wires|
        REF_WIRES_TO_DIGIT.key?(sample_wires.tr(tr_key, "abcdefg").each_char.sort.join)
      end
    end.join
  end
end

if __FILE__ == $0
  total = 0
  ARGF.each_line.map do |line|
    samples, digits = line.chomp.split(" | ").map(&:split)
    ssd = SevenSegmentDisplay.new(samples)
    numbers = Set.new([1, 4, 7, 8])
    total += digits.count { |digit| numbers.member?(ssd.translate_digit(digit)) }
  end
  puts(total)
end
