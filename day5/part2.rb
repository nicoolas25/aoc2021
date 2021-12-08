require "set"

Point = Struct.new(:x, :y)

Line = Struct.new(:a, :b) do
  def points
    @points ||= begin
      if a.x == b.x
        min, max = [a.y, b.y].minmax
        Set.new(min.upto(max).map { |y| Point.new(a.x, y) })
      elsif a.y == b.y
        min, max = [a.x, b.x].minmax
        Set.new(min.upto(max).map { |x| Point.new(x, a.y) })
      else
        min_x, max_x = [a.x, b.x].minmax
        min_y, max_y = [a.y, b.y].minmax
        raise NotImplementedError if max_x - min_x != max_y - min_y

        step_x = b.x <=> a.x
        step_y = b.y <=> a.y
        Set.new(
          0.upto(max_x - min_x).map do |step|
            Point.new(a.x + step_x * step, a.y + step_y * step)
          end
        )
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

overlaps = Set.new

lines.each do |line_a|
  lines.each do |line_b|
    next if line_a.object_id == line_b.object_id
    overlaps.merge(line_a.intersection(line_b))
  end
end

puts overlaps.size
