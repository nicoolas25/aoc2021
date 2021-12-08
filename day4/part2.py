from part1 import cache_by_id, read_inputs, sum_of_unmarked_numbers, wins_with_draw

def last_board_to_win(boards, full_draw):
    @cache_by_id
    def get_rows_and_cols(board):
        rows = [set(row) for row in board]
        cols = [set(row[col_index] for row in board) for col_index in range(len(board))]
        return (rows, cols)

    boards = boards.copy()
    for uppper_index in range(4, len(full_draw)):
        draw = full_draw[0:uppper_index]
        draw_set = set(draw)
        winning_boards = [
            board
            for board in boards
            if wins_with_draw(
                *get_rows_and_cols(board),
                draw_set
            )
        ]
        for winning_board in winning_boards:
            boards.remove(winning_board)
            get_rows_and_cols.clear(winning_board)
        if len(boards) == 0:
            return (winning_boards[0], draw)
    raise ValueError("Some board never wins")

if __name__ == "__main__":
    import fileinput

    # Toggling on and off the optimized data structure by switching to 'Board'.
    # The rest of the code can stay the same.
    full_draw, boards = read_inputs([line.strip() for line in fileinput.input()])
    board, draw = last_board_to_win(boards, full_draw)
    print(sum_of_unmarked_numbers(board, draw) * draw[-1])
