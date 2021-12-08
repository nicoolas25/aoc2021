import functools
from itertools import chain
from typing import Iterable, List, Tuple, Set

Board = List[List[int]]
Draw = List[int]
DrawSet = Set[int]

def cache_by_id(fn):
    cache = dict()

    @functools.wraps(fn)
    def cached_function(single_argument):
        cache_key = id(single_argument)
        if cache_key not in cache:
            cached_value = fn(single_argument)
            cache[cache_key] = cached_value
        else:
            cached_value = cache[cache_key]
        return cached_value

    def clear(single_argument):
        cache_key = id(single_argument)
        del cache[cache_key]

    cached_function.clear = clear

    return cached_function

def first_board_to_win(boards: List[Board], full_draw: Draw) -> Tuple[Board, Draw]:
    @cache_by_id
    def get_rows_and_cols(board):
        rows = [set(row) for row in board]
        cols = [set(row[col_index] for row in board) for col_index in range(len(board))]
        return (rows, cols)

    for uppper_index in range(4, len(full_draw)):
        draw = full_draw[0:uppper_index]
        draw_set = set(draw)
        for board in boards:
            rows, cols = get_rows_and_cols(board)
            if wins_with_draw(rows, cols, draw_set):
                return (board, draw)

    raise ValueError("No board ever wins")

def wins_with_draw(rows: Iterable[Set[int]], columns: Iterable[Set[int]], draw: DrawSet) -> bool:
    return any(line.issubset(draw) for line in chain(rows, columns))

def sum_of_unmarked_numbers(board: Board, draw: Draw) -> int:
    return sum(
        cell
        for row in board
        for cell in row
        if cell not in draw
    )

def read_inputs(lines) -> Tuple[Draw, List[Board]]:
    draw = [int(number) for number in lines[0].split(",")]
    boards = [
        [
            [int(cell) for cell in row.split()]
            for row in lines[index+1:index+6]
        ]
        for index in range(1, len(lines), 6)
    ]
    return (draw, boards)

if __name__ == "__main__":
    import fileinput

    full_draw, boards = read_inputs([line.strip() for line in fileinput.input()])
    board, draw = first_board_to_win(boards, full_draw)
    print(sum_of_unmarked_numbers(board, draw) * draw[-1])
