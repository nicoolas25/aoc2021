from part1 import (
    Board,
    DrawSet,
    board_wins_with,
    read_inputs,
    sum_of_unmarked_numbers,
)

class FastBoard:
    def __init__(self, board: Board):
        self.raw_board = board
        self.winning_sets = [
            *[ # Rows
                set(row)
                for row in board
            ],
            *[ # Cols
                set(row[col_index] for row in board)
                for col_index in range(len(board))
            ],
        ]

@board_wins_with.register
def fast_board__board_wins_with(board: FastBoard, numbers: DrawSet):
    return any(
        winning_set <= numbers
        for winning_set in board.winning_sets
    )

@sum_of_unmarked_numbers.register
def fast_board__sum_of_unmarked_numbers(board: FastBoard, numbers: DrawSet):
    return sum_of_unmarked_numbers(board.raw_board, numbers)


if __name__ == "__main__":
    import fileinput

    full_draw, raw_boards = read_inputs([line.strip() for line in fileinput.input()])
    boards = [FastBoard(board) for board in raw_boards]

    for uppper_index in range(4, len(full_draw)):
        draw = full_draw[0:uppper_index]
        draw_set = set(draw)
        winning_boards = [
            board
            for board in boards
            if board_wins_with(board, draw_set)
        ]
        for winning_board in winning_boards:
            boards.remove(winning_board)
        if not boards:
            last_winning_board = winning_boards[0]
            print(sum_of_unmarked_numbers(last_winning_board, draw_set) * draw[-1])
            break
