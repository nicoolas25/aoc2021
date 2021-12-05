if __name__ == "__main__":
    from part1 import read_inputs, sum_of_unmarked_numbers, board_wins_with

    import fileinput

    draws, boards = read_inputs([line.strip() for line in fileinput.input()])

    for uppper_index in range(4, len(draws)):
        numbers = draws[0:uppper_index]
        winning_boards = [
            board
            for board in boards
            if board_wins_with(board, numbers)
        ]
        for winning_board in winning_boards:
            boards.remove(winning_board)

        if not boards:
            last_winning_board = winning_boards[0]
            print(sum_of_unmarked_numbers(last_winning_board, numbers) * numbers[-1])
            break
