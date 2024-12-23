
from collections import deque


class ArcConsistency:
    def __init__(self):
        self.rows = 9
        self.cols = 9

    def setup_domains(self, board):
        domains = {}
        for r in range(self.rows):
            for c in range(self.cols):
                if board[r][c] == 0:
                    domains[(r, c)] = {1, 2, 3, 4, 5, 6, 7, 8, 9}
                else:
                    domains[(r, c)] = {board[r][c]}

        return domains

    def arc_consistency(self, domains, arcs):
        qu = deque(arcs)

        while qu:
            arc = qu.popleft()
            r, c = arc
            if self.check_arc(domains, arc):
                if not domains[r]:
                    return False

                for nei in self.get_neighbors(arcs, r):
                    if nei != c:
                        qu.append((nei, r))

        return True

    def get_arcs(self):
        arcs = []

        for r in range(self.rows):
            for c in range(self.cols):
                for k in range(c + 1, self.cols):
                    arcs.append(((r, c), (r, k)))
                    arcs.append(((c, r), (k, r)))

        for sub_row in range(0, self.rows, 3):
            for sub_col in range(0, self.cols, 3):
                sub_grid = []
                for r in range(3):
                    for c in range(3):
                        sub_grid.append((sub_row + r, sub_col + c))

                for r in range(len(sub_grid)):
                    for c in range(r + 1, len(sub_grid)):
                        arcs.append((sub_grid[r], sub_grid[c]))

        return arcs

    def get_neighbors(self, arcs, tile):
        neighbors = set()
        for r, c in arcs:
            if r == tile:
                neighbors.add(c)
            elif c == tile:
                neighbors.add(r)
        return neighbors

    def check_arc(self, domains, arc):
        r, c = arc
        flag = False
        not_valid = set()

        for val in domains[r]:
            tmp = True
            for other in domains[c]:
                if val != other:
                    tmp = False
                    break

            if tmp:
                not_valid.add(val)
                flag = True

        domains[r] -= not_valid
        return flag
