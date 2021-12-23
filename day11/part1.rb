require "set"

Position = Struct.new(:i, :j) do
  def neighbors(existing_positions)
    [
      Position.new(i, j + 1),
      Position.new(i, j - 1),
      Position.new(i + 1, j),
      Position.new(i - 1, j),
      Position.new(i + 1, j + 1),
      Position.new(i + 1, j - 1),
      Position.new(i - 1, j + 1),
      Position.new(i - 1, j - 1),
    ].select { |c| existing_positions.member?(c) }
  end
end

class Octopus
  attr_accessor :position
  attr_accessor :last_flash_step

  def initialize(energy_level)
    @energy_level = energy_level
    @last_fash_step = -1
  end

  def increase_energy_level!(for_step_number)
    if @last_fash_step < for_step_number
      @energy_level += 1
    end

    if @energy_level > 9
      @last_fash_step = for_step_number
      @energy_level = 0
      return true
    end

    false
  end
end

class Simulation
  attr_reader :flash_count

  def initialize
    @flash_count = 0
    @step_number = 0
    @octopuses = {}
    @positions = Set.new
    ARGF.each_line.each.with_index do |line, i|
      line.chomp.each_char.with_index do |energy_level, j|
        position = Position.new(i, j)
        @octopuses[position] = Octopus.new(energy_level.to_i)
        @positions << position
      end
    end
  end

  def tick
    @step_number += 1
    @positions.each do |position|
      increase_and_propagate_flashes!(position)
    end
  end

  private

  def increase_and_propagate_flashes!(position)
    positions_to_increase = [position]
    while positions_to_increase.any?
      position_to_increase = positions_to_increase.shift
      do_flash = @octopuses
        .fetch(position_to_increase)
        .increase_energy_level!(@step_number)
      if do_flash
        @flash_count += 1
        positions_to_increase.concat(
          position_to_increase.neighbors(@positions)
        )
      end
    end
  end
end

if __FILE__ == $0
  simulation = Simulation.new
  100.times { simulation.tick }
  puts(simulation.flash_count)
end
