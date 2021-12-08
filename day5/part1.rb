require "set"

Point = Struct.new(:x, :y)

Line = Struct.new(:a, :b) do
  def horizontal_or_vertical?
    a.x == b.x || a.y == b.y
  end

  def points
    @points ||= begin
      if a.x == b.x
        min, max = [a.y, b.y].minmax
        Set.new(min.upto(max).map { |y| Point.new(a.x, y) })
      elsif a.y == b.y
        min, max = [a.x, b.x].minmax
        Set.new(min.upto(max).map { |x| Point.new(x, a.y) })
      else
        raise NotImplementedError
      end
    end
  end

  def intersection(other_line)
    self.points & other_line.points
  end
end


lines = ARGF.each_line.map do |line|
  points = line.chomp.split(" -> ").map do |point_str|
    Point.new(*point_str.split(",").map(&:to_i))
  end
  Line.new(*points)
end

# Ignore some lines
lines.select!(&:horizontal_or_vertical?)

overlaps = Set.new

lines.each do |line_a|
  lines.each do |line_b|
    next if line_a.object_id == line_b.object_id
    overlaps.merge(line_a.intersection(line_b))
  end
end

puts overlaps.size
