import fileinput
from typing import Callable, List

def cost_part_1(x: int, numbers: List[int]) -> int:
    return sum(abs(x-n) for n in numbers)

def cost_part_2(x: int, numbers: List[int]) -> int:
    return sum(
        int(abs(x-n) * (abs(x-n) + 1) / 2)
        for n in numbers
    )

def reduce_cost(starting_point: int, numbers: List[int], cost_fn: Callable) -> int:
    cost = cost_fn(starting_point, numbers)
    left_cost = cost_fn(starting_point - 1, numbers)
    right_cost = cost_fn(starting_point + 1, numbers)
    if left_cost > cost and right_cost > cost:
        return cost
    elif left_cost < cost:
        return reduce_cost(starting_point - 1, numbers, cost_fn)
    else:
        return reduce_cost(starting_point + 1, numbers, cost_fn)

first_line = str(next(fileinput.input()).strip())
numbers = [int(i) for i in first_line.split(",")]
average = int(sum(numbers) / len(numbers))
print(reduce_cost(average, numbers, cost_part_1))
print(reduce_cost(average, numbers, cost_part_2))

