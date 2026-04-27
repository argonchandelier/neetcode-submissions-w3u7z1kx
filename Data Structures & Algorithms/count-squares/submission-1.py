from collections import defaultdict

class CountSquares:
    def __init__(self):
        self.rows = defaultdict(list)
        self.cols = defaultdict(list)

    def add(self, point: List[int]) -> None:
        self.rows[point[0]].append(point[1])
        self.cols[point[1]].append(point[0])       

    def count(self, point: List[int]) -> int:
        count = 0
        r0, c0 = point
        for c in self.rows[r0]:
            if c == c0:
                continue
            for r in self.cols[c]:
                if r == r0:
                    continue
                for c2 in self.rows[r]:
                    if c2 == c0:
                        count += 1
        return count
