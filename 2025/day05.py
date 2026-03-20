from common.base_solution import BaseSolution

class Range:
    def __init__(self, a: int, b: int):
        if a > b:
            raise ValueError("a must be <= b")
        self.a = a
        self.b = b

    def contains(self, v: int) -> bool:
        return self.a <= v <= self.b

    def overlaps(self, other: "Range") -> bool:
        return self.a <= other.b and other.a <= self.b

    def union(self, other: "Range") -> "Range | None":
        if not self.overlaps(other):
            return None
        return Range(min(self.a, other.a), max(self.b, other.b))

    def __eq__(self, other):
        return isinstance(other, Range) and self.a == other.a and self.b == other.b

    def __hash__(self) -> int:
        return hash((self.a, self.b))

class Solution(BaseSolution):
    def Part1(self) -> BaseSolution.ResultType:
        ranges_raw, ids = self.dataRaw.split("\n\n")
        ranges = [Range(*map(int, l.split('-'))) for l in ranges_raw.splitlines()]

        t = 0

        for id in map(int, ids.splitlines()):
            for r in ranges:
                if r.contains(id):
                    t += 1
                    break

        return t

    def Part2(self) -> int:
        self.dataRaw = "3-5\n10-14\n16-20\n12-18"
        ranges_raw = self.dataRaw.splitlines()
        ranges = [Range(*map(int, l.split('-'))) for l in ranges_raw]

        ranges.sort(key=lambda r: r.a)

        merged = []
        for r in ranges:
            if len(merged) == 0 or merged[-1].b < r.a:
                merged.append(r)
            else:
                merged[-1].b = max(merged[-1].b, r.b)

        t = 0
        for r in merged:
            t += r.b - r.a

        return t
