from typing import List, Tuple

Draw = List[int]
Board = List[List[int]]

def board_wins_with(board: Board, draw: Draw) -> bool:
    for row in board:
        if sum(cell in draw for cell in row) == len(board):
            return True
    for col_index in range(len(board)):
        if sum(row[col_index] in draw for row in board) == len(board):
            return True
    return False

def sum_of_unmarked_numbers(board: Board, draw: Draw) -> int:
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

    draws, boards = read_inputs([line.strip() for line in fileinput.input()])

    for uppper_index in range(4, len(draws)):
        numbers = draws[0:uppper_index]
        board = next(
            (board for board in boards if board_wins_with(board, numbers)),
            None,
        )
        if board:
            print(sum_of_unmarked_numbers(board, numbers) * numbers[-1])
            break
