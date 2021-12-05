from typing import Generator, List, Protocol, Tuple, Set, Type, TypeVar

Draw = List[int]
DrawSet = Set[int]

# The Protocol describe what we want to get from the data, it's not
# a behavior, more of an access layer. This specific access layer makes
# specific behaviors easier to implement and more readable BUT it risks
# bloating the data structure with many access layers that are useless
# or creating one datastructure per use-case and specific need.

class RowsAndColumns(Protocol):
    def rows(self) -> Generator[Set[int], None, None]:
        ...

    def columns(self) -> Generator[Set[int], None, None]:
        ...

def wins_with_draw(board: RowsAndColumns, draw: DrawSet) -> bool:
    return (
        any(row.issubset(draw) for row in board.rows())
        or any(col.issubset(draw) for col in board.columns())
    )

def sum_of_unmarked_numbers(board: RowsAndColumns, draw: Draw) -> int:
    return sum(
        number
        for row in board.rows()
        for number in row
        if number not in draw
    )

_S = TypeVar("_S", bound=RowsAndColumns)

def first_board_to_win(boards: List[_S], full_draw: Draw) -> Tuple[_S, Draw]:
    for uppper_index in range(4, len(full_draw)):
        draw = full_draw[0:uppper_index]
        draw_set = set(draw)
        for board in boards:
            if wins_with_draw(board, draw_set):
                return (board, draw)
    raise ValueError("No board ever wins")

class Board: # Implements RowsAndColumns from a matrix
    def __init__(self, matrix):
        self.matrix = matrix

    # We're building the same sets over and over again
    def rows(self):
        for row in self.matrix:
            yield set(row)

    def columns(self):
        for col_index in range(len(self.matrix)):
            yield set(row[col_index] for row in self.matrix)

_T = TypeVar("_T")

def read_inputs(lines, board_class: Type[_T]) -> Tuple[Draw, List[_T]]:
    draw = [int(number) for number in lines[0].split(",")]
    boards = [
        board_class([
            [int(cell) for cell in row.split()]
            for row in lines[index+1:index+6]
        ])
        for index in range(1, len(lines), 6)
    ]
    return (draw, boards)

if __name__ == "__main__":
    import fileinput

    full_draw, boards = read_inputs(
        [line.strip() for line in fileinput.input()],
        board_class=Board,
    )
    board, draw = first_board_to_win(boards, full_draw)
    print(sum_of_unmarked_numbers(board, draw) * draw[-1])
