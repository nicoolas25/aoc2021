Position = Struct.new(:horizontal, :depth) do
  def up(x)
    Position.new(horizontal, depth - x)
  end

  def down(x)
    Position.new(horizontal, depth + x)
  end

  def forward(x)
    Position.new(horizontal + x, depth)
  end
end

final_position = ARGF.each_line.reduce Position.new(0, 0) do |p, line|
  command, x = line.split
  p.public_send(command, x.to_i)
end

puts final_position.horizontal * final_position.depth
