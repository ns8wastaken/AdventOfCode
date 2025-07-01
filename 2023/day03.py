from common.base_solution import BaseSolution

class Solution(BaseSolution):
    def Part1(self) -> BaseSolution.ResultType:
        map = [list(line) for line in self.dataRaw.splitlines()]

        dirs = (
            (-1, -1), (0, -1), (1, -1),
            (-1,  0),          (1,  0),
            (-1,  1), (0,  1), (1,  1)
        )

        nums = dict() # coord: (num, coords that num covers)
        y = 0
        while y < len(map):
            x = 0
            while x < len(map[y]):
                if map[y][x].isdigit():
                    s = ""
                    coords = []

                    while x < len(map[y]) and map[y][x].isdigit():
                        s += map[y][x]
                        coords.append((x, y))
                        x += 1

                    n = int(s)
                    for c in coords:
                        nums[c] = (n, coords)

                else:
                    x += 1
            y += 1

        t = 0

        used = set()
        for cy in range(len(map)):
            for cx in range(len(map[cy])):
                c = map[cy][cx]
                if c != '.' and (not c.isdigit()):
                    for d in dirs:
                        nx, ny = cx + d[0], cy + d[1]
                        tup = (nx, ny)
                        if tup in nums and tup not in used:
                            n, coords = nums[tup]
                            t += n
                            for coords in coords:
                                used.add(coords)

        return t

    def Part2(self) -> BaseSolution.ResultType:
        map = [list(line) for line in self.dataRaw.splitlines()]

        dirs = (
            (-1, -1), (0, -1), (1, -1),
            (-1,  0),          (1,  0),
            (-1,  1), (0,  1), (1,  1)
        )

        nums = dict() # coord: (num, coords that num covers)
        y = 0
        while y < len(map):
            x = 0
            while x < len(map[y]):
                if map[y][x].isdigit():
                    s = ""
                    coords = []

                    while x < len(map[y]) and map[y][x].isdigit():
                        s += map[y][x]
                        coords.append((x, y))
                        x += 1

                    n = int(s)
                    for c in coords:
                        nums[c] = (n, coords)

                else:
                    x += 1
            y += 1

        t = 0

        for cy in range(len(map)):
            for cx in range(len(map[cy])):
                c = map[cy][cx]
                if c == '*':
                    l = []
                    used = set()
                    for d in dirs:
                        nx, ny = cx + d[0], cy + d[1]
                        tup = (nx, ny)
                        if tup in nums and tup not in used:
                            l.append((nx, ny))
                            for coords in nums[tup][1]:
                                used.add(coords)
                    if len(l) == 2:
                        t += nums[l[0]][0] * nums[l[1]][0]

        return t
