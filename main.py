from solver.sudoku_generation import SudokuPuzzleGeneration
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
    # board = [
    #     [0, 4, 2, 3, 0, 0, 0, 0, 5],
    #     [3, 0, 0, 1, 0, 5, 0, 4, 0],
    #     [0, 6, 1, 8, 2, 0, 0, 0, 0],
    #     [7, 0, 3, 0, 1, 0, 0, 2, 0],
    #     [0, 0, 0, 2, 4, 8, 9, 0, 0],
    #     [4, 0, 8, 0, 3, 9, 0, 0, 6],
    #     [0, 1, 0, 4, 0, 2, 7, 0, 9],
    #     [0, 3, 0, 0, 0, 0, 4, 8, 2],
    #     [2, 0, 0, 0, 0, 3, 6, 5, 0]
    # board = [
    #     [0, 0, 0, 7, 0, 2, 9, 0, 0],
    #     [0, 9, 0, 0, 8, 1, 2, 0, 0],
    #     [8, 7, 2, 4, 5, 0, 0, 1, 3],
    #     [1, 0, 0, 0, 7, 0, 4, 2, 0],
    #     [9, 0, 0, 1, 0, 5, 0, 0, 8],
    #     [0, 4, 0, 0, 0, 0, 5, 6, 0],
    #     [0, 3, 5, 8, 0, 4, 0, 9, 6],
    #     [0, 8, 0, 0, 3, 6, 7, 0, 0],
    #     [0, 0, 0, 5, 0, 0, 0, 3, 2]
    # ]

    # board = [
    #     [6, 0, 0, 0, 5, 0, 1, 0, 0],
    #     [0, 3, 0, 0, 9, 0, 0, 4, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 5, 0, 0, 3, 0, 6, 0, 0],
    #     [0, 8, 0, 0, 0, 0, 2, 0, 0],
    #     [0, 4, 0, 5, 8, 0, 0, 0, 1],
    #     [3, 0, 0, 0, 0, 9, 0, 0, 2],
    #     [7, 0, 0, 0, 1, 0, 9, 0, 0],
    #     [0, 0, 0, 2, 0, 8, 0, 0, 0],
    # ]
    # board = [
    #     [8, 0, 0, 1, 5, 7, 0, 9, 0],
    #     [0, 0, 6, 2, 0, 0, 0, 5, 0],
    #     [0, 0, 0, 3, 9, 0, 0, 0, 0],
    #     [0, 8, 0, 6, 7, 0, 0, 3, 1],
    #     [0, 5, 0, 0, 0, 0, 0, 0, 9],
    #     [6, 0, 3, 0, 0, 9, 0, 2, 0],
    #     [3, 0, 0, 4, 1, 0, 0, 0, 0],
    #     [0, 0, 9, 0, 6, 0, 1, 0, 0],
    #     [0, 0, 1, 0, 0, 0, 0, 7, 4],
    # ]

    # solver = SudokuSolver(board)
    # result = solver.solve()

    # print_board(board)
    # print('\n\n', '=' * 10, "SOLVING", '=' * 10, '\n\n')
    # print_result(result)
    gen = SudokuPuzzleGeneration()
    board, solution = gen.generate_board('hard')

    print_board(board)
    print('\n\n', '=' * 10, "SOLVING", '=' * 10, '\n\n')
    print_result(solution)


if __name__ == '__main__':
    main()
