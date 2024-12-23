from solver.sudoku_solver import SudokuSolver


def print_board(board):
    for r in range(len(board)):
        if r > 0 and r % 3 == 0:
            print('-' * 22)
        for c in range(len(board[r])):
            if c > 0 and c % 3 == 0:
                print('|', end=' ')
            print(board[r][c], end=' ')
        print()


def print_result(solution):
    if not solution:
        print("No solution exists.")
    else:
        board = [[0] * 9 for _ in range(9)]
        for (i, j), value in solution.items():
            board[i][j] = value
        # for row in board:
        #     print(" ".join(str(x) for x in row))
        print_board(board)


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

    print_board(board)
    print('\n\n', '=' * 10, "SOLVING", '=' * 10, '\n\n')
    print_result(result)


if __name__ == '__main__':
    main()
