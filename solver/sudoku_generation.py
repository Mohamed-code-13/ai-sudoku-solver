import random
from solver.arc_consistency import ArcConsistency
from solver.sudoku_solver import SudokuSolver


class SudokuPuzzleGeneration:
    def __init__(self):
        self.rows = 9
        self.cols = 9

        self.empty_board = [[0] * self.cols for _ in range(self.rows)]

        self.arc = ArcConsistency()
        self.solver = SudokuSolver(self.empty_board)

        self.difficulty = {
            'easy': 30,
            'medium': 40,
            'hard': 50
        }

    def generate_solution(self):
        domains = self.arc.setup_domains(self.empty_board)
        arcs = self.arc.get_arcs()

        if self.arc.arc_consistency(domains, arcs):
            return self.solver.backtracking_with_randomniss(domains, arcs)
        return None

    def remove_tiles(self, solution, dif):
        no_to_remove = self.difficulty[dif]
        board = [[solution[(r, c)] for c in range(self.cols)]
                 for r in range(self.rows)]

        tiles = [(r, c) for r in range(self.rows) for c in range(self.cols)]
        random.shuffle(tiles)

        for r, c in tiles:
            if no_to_remove <= 0:
                break

            tmp = board[r][c]

            board[r][c] = 0

            self.solver.board = board
            if self.solver.has_unique_solution():
                no_to_remove -= 1
            else:
                board[r][c] = tmp

        return board

    def generate_board(self, dif):
        sol = self.generate_solution()
        if not sol:
            raise ValueError('Error in generation solution')

        board = self.remove_tiles(sol, dif)
        return board, sol
