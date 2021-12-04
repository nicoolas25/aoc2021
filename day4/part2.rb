require "set"

class Board
  def initialize(matrix)
    @matrix = matrix
    @winning_sets = (matrix + matrix.transpose)
      .map { |row_or_col| Set.new(row_or_col) }
  end

  def solved_with?(numbers)
    @winning_sets.any? { |winning_set| numbers >= winning_set }
  end

  def unmarked_numbers_sum(numbers)
    @matrix.sum do |row|
      row.sum do |cell|
        numbers.member?(cell) ? 0 : cell
      end
    end
  end
end

lines = ARGF.each_line.map(&:chomp).to_a
draw = lines.shift.split(",").map(&:to_i)
boards = lines.each_slice(6).map do |rows|
  Board.new(rows[1..].map { |row| row.split.map(&:to_i) })
end

(5..draw.size).each do |numbers_count|
  numbers = draw.first(numbers_count)
  numbers_set = Set.new(numbers)
  winning_boards = boards.select { |board| board.solved_with?(numbers_set) }
  boards = boards - winning_boards
  if boards.empty?
    puts(winning_boards.first.unmarked_numbers_sum(numbers_set) * numbers.last)
    return
  end
end
