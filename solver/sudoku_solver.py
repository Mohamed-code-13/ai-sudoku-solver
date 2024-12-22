
import random
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

    def backtracking_with_randomniss(self, domains, arcs):
        if self.is_solved(domains):
            return self.convert_domain_to_solution(domains)

        tile = self.get_min_remaining_value(domains)
        if not tile:
            return None

        vals = sorted(domains[tile])
        random.shuffle(vals)
        for val in vals:
            new_domains = self.copy_domains(domains)
            new_domains[tile] = {val}

            if self.arc.arc_consistency(new_domains, arcs):
                res = self.backtracking_with_randomniss(new_domains, arcs)
                if res:
                    return res

        return None

    def is_solved(self, domains):
        for _, v in domains.items():
            if len(v) != 1:
                return False
        return True

    def has_unique_solution(self):
        domains = self.arc.setup_domains(self.board)
        arcs = self.arc.get_arcs()

        no_solutions = self.count_solutions(domains, arcs, 0)
        return no_solutions == 1

    def count_solutions(self, domains, arcs, count):
        if count > 1:
            return count

        if self.is_solved(domains):
            return count + 1

        tile = self.get_min_remaining_value(domains)
        if not tile:
            return count

        for val in sorted(domains[tile]):
            new_domains = self.copy_domains(domains)
            new_domains[tile] = {val}

            if self.arc.arc_consistency(new_domains, arcs):
                count = self.count_solutions(new_domains, arcs, count)

        return count

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
