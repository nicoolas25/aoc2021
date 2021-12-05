from part1 import read_inputs, sum_of_unmarked_numbers, wins_with_draw

# Unrelated to Board itself, FastBoard implements RowsAndColumns
# implicitly but optimize for accessing rows and columns sets.
#
# To make this optimization, we needed to rework the part1 to
# find a common ground between implementations that could be reused.
# This wasn't necessary with singledispatch where we could overload
# some functions directly.
class FastBoard:
    def __init__(self, matrix):
        # Optimize for those row and column access right from the __init__
        self._rows = [set(row) for row in matrix]
        self._columns = [
            set(row[col_index] for row in matrix)
            for col_index in range(len(matrix))
        ]

    def rows(self):
        yield from self._rows

    def columns(self):
        yield from self._columns

def last_board_to_win(boards, full_draw):
    boards = boards.copy()
    for uppper_index in range(4, len(full_draw)):
        draw = full_draw[0:uppper_index]
        draw_set = set(draw)

        winning_boards = [
            board
            for board in boards
            if wins_with_draw(board, draw_set)
        ]
        for winning_board in winning_boards:
            boards.remove(winning_board)

        if len(boards) == 0:
            return (winning_boards[0], draw)
    raise ValueError("Some board never wins")

if __name__ == "__main__":
    import fileinput

    # Toggling on and off the optimized data structure by switching to 'Board'.
    # The rest of the code can stay the same.
    full_draw, boards = read_inputs(
        [line.strip() for line in fileinput.input()],
        board_class=FastBoard,
    )
    board, draw = last_board_to_win(boards, full_draw)
    print(sum_of_unmarked_numbers(board, draw) * draw[-1])
