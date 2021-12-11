from collections import defaultdict
from dataclasses import dataclass
from typing import Iterable, List, Tuple

@dataclass(frozen=True)
class Point:
    x: int
    y: int

Segment = Tuple[Point, Point]

def cmp(x, y):
    return (x > y) - (x < y)

def points_on_segment(segment: Segment) -> Iterable[Point]:
    a, b = segment
    step_x = cmp(b.x, a.x)
    step_y = cmp(b.y, a.y)
    return (
        Point(a.x + step_x * i, a.y + step_y * i)
        for i in range(max(abs(a.x - b.x), abs(a.y - b.y)) + 1)
    )

def read_inputs(lines) -> List[Segment]:
    segments = []
    for line in lines:
        segments.append(
            tuple([
                Point(*map(int, point_str.split(",")))
                for point_str in line.split(" -> ")
            ])
        )
    return segments

if __name__ == "__main__":
    import fileinput
    segments = read_inputs([line.strip() for line in fileinput.input()])
    counter = defaultdict(int)
    for segment in segments:
        for point in points_on_segment(segment):
            counter[point] += 1
    print(sum(count >= 2 for count in counter.values()))
