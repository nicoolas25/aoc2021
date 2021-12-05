from functools import singledispatch
from typing import List, Tuple, Set

Draw = List[int]
DrawSet = Set[int]
Board = List[List[int]]

@singledispatch
def board_wins_with(board: Board, draw: DrawSet) -> bool:
    for row in board:
        if sum(cell in draw for cell in row) == len(board):
            return True
    for col_index in range(len(board)):
        if sum(row[col_index] in draw for row in board) == len(board):
            return True
    return False

@singledispatch
def sum_of_unmarked_numbers(board: Board, draw: DrawSet) -> int:
    return sum(
        sum(cell for cell in row if cell not in draw)
        for row in board
    )

# ====

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

    for uppper_index in range(4, len(full_draw)):
        draw = full_draw[0:uppper_index]
        draw_set = set(draw)
        board = next(
            (board for board in boards if board_wins_with(board, draw_set)),
            None,
        )
        if board:
            print(sum_of_unmarked_numbers(board, draw_set) * draw[-1])
            break
