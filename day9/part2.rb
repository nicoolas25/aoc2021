require "set"
require "./part1"

class Map
  def initialize(matrix)
    @_coordinates_to_basin = {}
    @_basin_to_coordinates = {}
    matrix.each.with_index do |row, i|
      row.each.with_index do |cell, j|
        basin = Object.new
        coordinate = Coordinate.new(i, j)
        @_coordinates_to_basin[coordinate] = basin
        @_basin_to_coordinates[basin] = [coordinate]
      end
    end
  end

  def join(coordinate1, coordinate2)
    basin1 = @_coordinates_to_basin.fetch(coordinate1)
    basin2 = @_coordinates_to_basin.fetch(coordinate2)
    return if basin1 == basin2

    # Merge basin for both coordinates
    basin3 = Object.new
    @_basin_to_coordinates[basin3] = @_basin_to_coordinates.delete(basin1) + @_basin_to_coordinates.delete(basin2)
    @_basin_to_coordinates[basin3].each do |coordinate|
      @_coordinates_to_basin[coordinate] = basin3
    end
  end

  def basins
    @_basin_to_coordinates.values
  end
end

if __FILE__ == $0
  matrix = ARGF.each_line.map { |line| line.chomp.each_char.map(&:to_i) }
  map = Map.new(matrix)
  matrix.each.with_index do |row, i|
    row.each.with_index do |value, j|
      next if matrix[i][j] == 9

      coordinate = Coordinate.new(i, j)
      accessible_coordinates = coordinate
        .neighbors_coordinates(matrix.size, row.size)
        .reject { |c| matrix[c.i][c.j] == 9 }
        .each { |c| map.join(coordinate, c) }
    end
  end
  a, b, c = map.basins.map(&:size).sort.last(3)
  puts(a * b * c)
end
