from typing import Iterable, Set

from part1 import Position, neighbors

class BasinsMap:
    def __init__(self, positions: Iterable[Position]):
        self._basin_by_position = {p: set([p]) for p in positions}

    def link(self, position_1: Position, position_2: Position) -> None:
        basin_1 = self._basin_by_position[position_1]
        basin_2 = self._basin_by_position[position_2]

        if id(basin_1) == id(basin_2):
            return None

        basin_3 = basin_1.union(basin_2)
        for position in basin_3:
            self._basin_by_position[position] = basin_3

    def __iter__(self) -> Iterable[Set[Position]]:
        uniq_basins = {
            id(basin): basin
            for basin in self._basin_by_position.values()
        }
        yield from uniq_basins.values()

if __name__ == "__main__":
    import fileinput

    positions = {
        Position(i, j)
        for i, line in enumerate(fileinput.input())
        for j, cell in enumerate(line.strip())
        if cell != "9"
    }

    basins = BasinsMap(positions)

    for position in positions:
        for n in neighbors(positions, position):
            basins.link(position_1=position, position_2=n)

    a, b, c = sorted(map(len, basins))[-3:]
    print(a * b * c)
