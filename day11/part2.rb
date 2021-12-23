require "./part1"

class Part2Simulation <  Simulation
  attr_reader :step_number

  def tick
    @previous_flash_count = @flash_count
    super
  end

  def all_octopuses_just_flashed?
    return false unless defined?(@previous_flash_count)

    (@flash_count - @previous_flash_count) == @positions.size
  end
end

if __FILE__ == $0
  simulation = Part2Simulation.new
  simulation.tick until simulation.all_octopuses_just_flashed?
  puts(simulation.step_number)
end
