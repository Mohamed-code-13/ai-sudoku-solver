
from solver.arc_consistency import ArcConsistency


class SudokuSolver:
    def __init__(self, board):
        self.board = board

        self.arc = ArcConsistency()

    def solve(self):
        return self.board
