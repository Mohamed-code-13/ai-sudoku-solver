
from solver.arc_consistency import ArcConsistency


class SudokuSolver:
    def __init__(self, board):
        self.board = board

        self.arc = ArcConsistency()

    def solve(self):
        arcs = self.arc.get_arcs()
        domains = self.arc.setup_domains(self.board)

        if self.arc.arc_consistency(domains, arcs):
            return self.backtracking(domains, arcs)
        return None

    def backtracking(self, domains, arcs):
        if self.is_solved(domains):
            return self.convert_domain_to_solution(domains)

        tile = self.get_min_remaining_value(domains)
        if not tile:
            return None

        for val in sorted(domains[tile]):
            new_domains = self.copy_domains(domains)
            new_domains[tile] = {val}

            if self.arc.arc_consistency(new_domains, arcs):
                res = self.backtracking(new_domains, arcs)
                if res:
                    return res

        return None

    def is_solved(self, domains):
        for _, v in domains.items():
            if len(v) != 1:
                return False
        return True

    def get_min_remaining_value(self, domains):
        possibles = []
        for tile, vals in domains.items():
            if len(vals) > 1:
                possibles.append(tile)

        min_value = float('inf')
        res = None
        for p in possibles:
            if len(domains[p]) < min_value:
                min_value = len(domains[p])
                res = p

        return res

    def convert_domain_to_solution(self, domains):
        solution = {}
        for k, v in domains.items():
            for out in v:
                solution[k] = out
        return solution

    def copy_domains(self, domains):
        new_domains = {}

        for k, v in domains.items():
            new_domains[k] = set(v)

        return new_domains
