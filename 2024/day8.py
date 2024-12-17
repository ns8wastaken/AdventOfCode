from common.base_solution import BaseSolution
from utils.vector2 import Vec2
from collections import defaultdict


class Solution(BaseSolution):
    def Part1(self) -> int:
        data = [list(i) for i in self.dataRaw.split("\n")]

        width  = len(data[0])
        height = len(data)

        usedChars = dict()

        for y in range(height):
            for x in range(width):
                c = data[y][x]
                if c != "." and c != "\n":
                    usedChars.setdefault(c, [])
                    usedChars[c].append(Vec2(x, y))

        locs = set()

        for c, coords in usedChars.items():
            for i in range(len(coords)):
                for j in range(i + 1, len(coords)):
                    vi, vj = coords[i], coords[j]
                    v = vj - vi

                    v = vj - vi

                    l1 = vj + v
                    if 0 <= l1.x < width and 0 <= l1.y < height:
                        locs.add(l1)

                    l2 = vi - v
                    if 0 <= l2.x < width and 0 <= l2.y < height:
                        locs.add(l2)

        return len(locs)

    def Part2(self) -> int:
        data = [list(row) for row in self.dataRaw.split("\n")]
        width, height = len(data[0]), len(data)

        usedChars: dict[str, list[Vec2]] = defaultdict(list)
        for y in range(height):
            for x in range(width):
                c = data[y][x]
                if c not in (".", "\n"):
                    usedChars[c].append(Vec2(x, y))

        locs = set()

        for c, coords in usedChars.items():
            n = len(coords)
            if n < 2:
                continue

            for i in range(n):
                for j in range(i + 1, n):
                    vi, vj = coords[i], coords[j]
                    v = vj - vi

                    locs.add(vi)
                    locs.add(vj)

                    for direction in (-1, 1):
                        idx = 1
                        current = vj + v * direction
                        while 0 <= current.x < width and 0 <= current.y < height:
                            locs.add(current)
                            idx += 1
                            current = vj + v * direction * idx

        return len(locs)
