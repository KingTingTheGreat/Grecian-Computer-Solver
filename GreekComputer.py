from Ring import Ring, COLUMNS

RING_ONE = [[7, None, 15, None, 8, None, 3, None, 6, None, 10, None]]

RING_TWO = [
    [11, 6, 11, None, 6, 17, 7, 3, None, 6, None, 11],
    [14, None, 9, None, 12, None, 4, None, 7, 15, None, None],
]

RING_THREE = [
    [9, 7, 13, 21, 17, 4, 5, None, 7, 8, 9, 13],
    [15, 4, 9, 18, 11, 26, 14, 1, 12, None, 21, 6],
    [10, None, 8, None, 22, None, 16, None, 9, None, 5, None],
]

RING_FOUR = [
    [8, None, 16, 2, 7, None, 9, None, 7, 14, 11, None],
    [3, 8, 9, None, 9, 20, 12, 3, 6, None, 14, 12],
    [17, 19, 3, 12, 3, 26, 6, None, 2, 13, 9, None],
    [10, None, 10, None, 1, None, 9, None, 12, None, 6, None],
]

RING_FIVE = [
    [11, 11, 14, 11, 14, 11, 14, 14, 11, 14, 11, 14],
    [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
    [4, 4, 6, 6, 3, 3, 14, 14, 21, 21, 9, 9],
    [8, 3, 4, 12, 2, 5, 10, 7, 16, 8, 7, 8],
]

GOAL = 42


class GreekComputer:
    def __init__(self):
        self.base = Ring(RING_FIVE)
        self.rings = [
            Ring(RING_ONE),
            Ring(RING_TWO),
            Ring(RING_THREE),
            Ring(RING_FOUR),
        ]
        self.rows = max(len(ring) for ring in self.rings)
        self.unmutable = tuple(self.rings)

    def __repr__(self):
        cols = [self.get_str_col(i) for i in range(COLUMNS)]

        rows = []
        for i in range(self.rows):
            rows.append("\t".join(col[i] for col in cols))

        return "\n".join(rows[::-1])

    def get_col(self, i: int) -> list[int]:
        """returns the ith column"""
        vals = [None] * self.rows
        for ring in self.rings + [self.base]:
            for j, row in enumerate(ring):
                if row[i] is not None and vals[j] is None:
                    vals[j] = row[i]
        return vals

    def get_str_col(self, i: int) -> list[str]:
        """returns a string of the ith column"""
        vals = [None] * self.rows
        r = self.rings + [self.base]
        for depth, ring in enumerate(r):
            for j, row in enumerate(ring):
                if row[i] is not None and vals[j] is None:
                    vals[j] = "]" * (len(self.rings + [self.base]) - depth) + str(
                        row[i]
                    )
        return vals

    def is_solved(self) -> bool:
        """returns True if the puzzle is solved, False otherwise"""
        return all(sum(self.get_col(i)) == GOAL for i in range(COLUMNS))

    def permute(self, rings=None):
        """generates all permutations of the puzzle"""
        # default call
        if rings is None:
            rings = self.rings
        if not rings:
            yield [self.base]
            return
        ring = rings[0]
        for _ in range(COLUMNS):
            for rest in self.permute(rings[1:]):
                yield [ring] + rest
            ring.rotate()

    def solve(self) -> None:
        """solves the puzzle in place"""

        for p in self.permute():
            self.rings = p[:-1]  # base is not part of the rings
            if self.is_solved():
                return
        raise Exception("No solution found")
