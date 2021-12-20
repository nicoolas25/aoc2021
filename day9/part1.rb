Coordinate = Struct.new(:i, :j) do
  def neighbors_coordinates(limit_i, limit_j)
    [
      Coordinate.new(i, j + 1),
      Coordinate.new(i, j - 1),
      Coordinate.new(i + 1, j),
      Coordinate.new(i - 1, j),
    ].select { |c| c.i < limit_i && c.j < limit_j && c.i >= 0 && c.j >= 0 }
  end
end

if __FILE__ == $0
  total = 0
  matrix = ARGF.each_line.map { |line| line.chomp.each_char.map(&:to_i) }
  matrix.each.with_index do |row, i|
    row.each.with_index do |cell, j|
      neighbors_coordinates = Coordinate.new(i, j).neighbors_coordinates(matrix.size, row.size)
      if neighbors_coordinates.all? { |c| cell < matrix[c.i][c.j] }
        total += cell + 1
      end
    end
  end
  puts(total)
end
