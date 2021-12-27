from dataclasses import dataclass
from typing import Callable, Container, Dict, Iterable

@dataclass(frozen=True)
class Position:
    i: int
    j: int

@dataclass(frozen=True)
class Octopus:
    energy_level: int

OctopusesMap = Dict[Position, Octopus]

def neighbors(positions: Container[Position], position: Position) -> Iterable[Position]:
    return filter(
        lambda p: p in positions,
        [
            Position(position.i, position.j + 1),
            Position(position.i, position.j - 1),
            Position(position.i + 1, position.j),
            Position(position.i - 1, position.j),
            Position(position.i + 1, position.j + 1),
            Position(position.i + 1, position.j - 1),
            Position(position.i - 1, position.j + 1),
            Position(position.i - 1, position.j - 1),
        ]
    )

def step(octopuses: OctopusesMap, on_flash: Callable) -> OctopusesMap:
    octopuses = octopuses.copy()
    positions_to_reset = set()

    # Increase and propagate flashes for each positions
    for position in octopuses.keys():
        positions_to_increase = [position]
        while positions_to_increase:
            position_to_increase, *positions_to_increase = positions_to_increase
            did_flash = _increase_energy_level(octopuses, position_to_increase)
            if did_flash:
                positions_to_reset.add(position_to_increase)
                neighbors_to_increase = neighbors(positions=octopuses, position=position_to_increase)
                positions_to_increase.extend(neighbors_to_increase)

                if on_flash:
                    on_flash()

    # Reset the octopus that flashed after a step
    for position_to_reset in positions_to_reset:
        octopuses[position_to_reset] = Octopus(energy_level=0)

    return octopuses

def _increase_energy_level(
    octopuses: OctopusesMap,
    position: Position,
    max_energy_level: int = 10,
) -> bool:
    octopus = octopuses[position]
    if octopus.energy_level < max_energy_level:
        octopuses[position] = Octopus(octopus.energy_level + 1)
        return octopus.energy_level + 1 == max_energy_level
    return False

if __name__ == "__main__":
    import fileinput

    octopuses = {
        Position(i, j): Octopus(energy_level=int(cell))
        for i, line in enumerate(fileinput.input())
        for j, cell in enumerate(line.strip())
    }

    flash_count = 0
    def on_flash():
        nonlocal flash_count
        flash_count += 1

    for _ in range(100):
        octopuses = step(octopuses, on_flash)

    print(flash_count)
