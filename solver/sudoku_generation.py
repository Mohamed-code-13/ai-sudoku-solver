from solver.arc_consistency import ArcConsistency
from solver.sudoku_solver import SudokuSolver


class SudokuPuzzleGeneration:
    def __init__(self):
        self.rows = 9
        self.cols = 9
        self.empty_board = [[0] * self.cols for _ in range(self.rows)]

        self.arc = ArcConsistency()
        self.solver = SudokuSolver(self.empty_board)

    def generate_solution(self):
        domains = self.arc.setup_domains(self.empty_board)
        arcs = self.arc.get_arcs()

        if self.arc.arc_consistency(domains, arcs):
            return self.solver.backtracking_with_randomniss(domains, arcs)
        return None
