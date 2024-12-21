from solver.sudoku_solver import SudokuSolver


def print_result(board):
    for row in board:
        print(row)


def main():
    board = [
        [0, 4, 2, 3, 0, 0, 0, 0, 5],
        [3, 0, 0, 1, 0, 5, 0, 4, 0],
        [0, 6, 1, 8, 2, 0, 0, 0, 0],
        [7, 0, 3, 0, 1, 0, 0, 2, 0],
        [0, 0, 0, 2, 4, 8, 9, 0, 0],
        [4, 0, 8, 0, 3, 9, 0, 0, 6],
        [0, 1, 0, 4, 0, 2, 7, 0, 9],
        [0, 3, 0, 0, 0, 0, 4, 8, 2],
        [2, 0, 0, 0, 0, 3, 6, 5, 0]
    ]

    solver = SudokuSolver(board)
    result = solver.solve()

    print_result(result)


if __name__ == '__main__':
    main()
