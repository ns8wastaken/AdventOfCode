from common.base_solution import BaseSolution
from utils.vector2 import Vec2


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
            for i in coords:
                for j in coords:
                    if i == j: continue

                    v = j - i

                    l1 = j + v
                    if 0 <= l1.x < width and 0 <= l1.y < height:
                        locs.add(l1)

                    l2 = i - v
                    if 0 <= l2.x < width and 0 <= l2.y < height:
                        locs.add(l2)

        return len(locs)

    def Part2(self) -> int:
        d = "............\n........0...\n.....0......\n.......0....\n....0.......\n......A.....\n............\n............\n........A...\n.........A..\n............\n............"
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
            for i in coords:
                for j in coords:
                    if i == j: continue

                    v = j - i

                    idx = 1
                    l1 = j + v
                    while 0 <= l1.x < width and 0 <= l1.y < height:
                        locs.add(l1)
                        idx += 1
                        l1 = j + v * idx

                    if idx > 1:
                        locs.add(i)

                    idx = 1
                    l2 = j + v
                    while 0 <= l2.x < width and 0 <= l2.y < height:
                        locs.add(l2)
                        idx += 1
                        l2 = j + v * idx

                    if idx > 1:
                        locs.add(i)

        return len(locs)
