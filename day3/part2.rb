class Sequence
  ONE = "1"
  ZERO = "0"

  attr_reader :size

  def initialize(lines)
    @lines = lines
    @size = lines.size
    @bits = lines.first.size
    @majority = (lines.size / 2.0).ceil
  end

  def oxigen
    reduce_with(:select_majority).first.to_i(2)
  end

  def co2
    reduce_with(:reject_majority).first.to_i(2)
  end

  protected

  def reduce_with(method)
    (0...@bits).to_a.reduce(self) do |seq, index|
      seq.__send__(method, index).tap do |new_seq|
        return new_seq if new_seq.size == 1
      end
    end
  end

  def first
    @lines[0]
  end

  def select_majority(index)
    majority_bit = majority_bit_at(index)
    Sequence.new(@lines.select { |line| line[index] == majority_bit })
  end

  def reject_majority(index)
    majority_bit = majority_bit_at(index)
    Sequence.new(@lines.reject { |line| line[index] == majority_bit })
  end

  def majority_bit_at(index)
    one_count = @lines.count { |line| line[index] == ONE }
    one_count >= @majority ? ONE : ZERO
  end
end

seq = Sequence.new(ARGF.each_line.map(&:chomp).to_a)
puts seq.oxigen * seq.co2
