
import random
from solver.arc_consistency import ArcConsistency


class SudokuSolver:
    def __init__(self, board):
        self.board = board
        self.step_count = 0

        self.arc = ArcConsistency()
        self.previous_domains = {}

    def solve(self):
        self.step_count = 0
        arcs = self.arc.get_arcs()
        domains = self.arc.setup_domains(self.board)

        self.initialize_output_file()

        if self.arc.arc_consistency(domains, arcs):
            return self.backtracking(domains, arcs)
        return None

    def backtracking(self, domains, arcs):
        if self.is_solved(domains):
            return self.convert_domain_to_solution(domains)

        tile = self.get_min_remaining_value(domains)
        if not tile:
            return None

        lcv_order = self.least_constraining_value(domains, tile, arcs)

        for val in lcv_order:
            new_domains = self.copy_domains(domains)
            new_domains[tile] = {val}

            if self.arc.arc_consistency(new_domains, arcs):
                self.step_tracker(new_domains)
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

        lcv_order = self.least_constraining_value(domains, tile, arcs)

        for val in lcv_order:
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

    def least_constraining_value(self, domains, tile, arcs):
        values = domains[tile]
        return sorted(values, key=lambda x: self.count_constrains(domains, tile, arcs, x))

    def count_constrains(self, domains, tile, arcs, value):
        res = 0
        for nei in self.arc.get_neighbors(arcs, tile):
            if len(domains[nei]) > 1 and value in domains[nei]:
                res += 1
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

    def initialize_output_file(self):
        with open('domains.txt', "w") as f:
            f.write("Sudoku Domains Progression\n")
            f.write("=" * 81 + "\n\n")

    def save_domains_to_file(self, domains, filename, step_count):
        with open(filename, "a") as file:
            file.write(f"Step {step_count}:\n")
            file.write(self.format_domains(domains))
            file.write("\n")

    def format_domains(self, affected_domains):
        output = ""
        for tile, change in affected_domains.items():
            r, c = tile
            before = ", ".join(map(str, sorted(change['before'])))
            after = ", ".join(map(str, sorted(change['after'])))
            output += f"Cell ({r}, {c}): Before: [{
                before}] -> After: [{after}]\n"
        return output

    def get_affected_domains(self, current_domains):
        affected = {}
        for tile, values in current_domains.items():
            if tile not in self.previous_domains or self.previous_domains[tile] != values:
                affected[tile] = {
                    'before': self.previous_domains.get(tile, set()),
                    'after': values
                }
        return affected

    def step_tracker(self, current_domains):
        self.step_count += 1
        output_file = 'domains.txt'

        affected_domains = self.get_affected_domains(current_domains)
        self.save_domains_to_file(
            affected_domains, output_file, self.step_count)
        self.previous_domains = self.copy_domains(current_domains)
