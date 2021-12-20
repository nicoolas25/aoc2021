from dataclasses import dataclass
from functools import partial
from typing import Container, Iterable

@dataclass(frozen=True)
class Position:
    i: int
    j: int

def neighbors(positions: Container[Position], position: Position) -> Iterable[Position]:
    if (p := Position(position.i, position.j + 1)) in positions:
        yield p
    if (p := Position(position.i, position.j - 1)) in positions:
        yield p
    if (p := Position(position.i + 1, position.j)) in positions:
        yield p
    if (p := Position(position.i - 1, position.j)) in positions:
        yield p

if __name__ == "__main__":
    import fileinput

    positions = {
        Position(i, j): int(cell)
        for i, line in enumerate(fileinput.input())
        for j, cell in enumerate(line.strip())
    }

    print(sum(
        value + 1
        for position, value in positions.items()
        if all(value < positions[n] for n in neighbors(positions, position))
    ))
