from common.base_solution import BaseSolution

class Solution(BaseSolution):
    def Part1(self) -> BaseSolution.ResultType:
        universe = self.dataRaw.splitlines()
        height, width = len(universe), len(universe[0])

        galaxies = []
        empty_cols = [True for _ in range(width)]
        empty_rows = [True for _ in range(height)]

        for y in range(height):
            for x in range(width):
                if universe[y][x] == '#':
                    empty_cols[x] = False
                    empty_rows[y] = False
                    galaxies.append((x, y))

        empty_cols_before = [0 for _ in range(width + 1)]
        for x in range(width):
            empty_cols_before[x + 1] = empty_cols_before[x] + empty_cols[x]

        empty_rows_before = [0 for _ in range(height + 1)]
        for y in range(height):
            empty_rows_before[y + 1] = empty_rows_before[y] + empty_rows[y]

        t = 0
        n = len(galaxies)
        for i in range(n - 1):
            g1 = galaxies[i]

            for j in range(i + 1, n):
                g2 = galaxies[j]

                minx, maxx = min(g1[0], g2[0]), max(g1[0], g2[0])
                miny, maxy = min(g1[1], g2[1]), max(g1[1], g2[1])

                t += maxx - minx + maxy - miny
                t += empty_cols_before[maxx] - empty_cols_before[minx]
                t += empty_rows_before[maxy] - empty_rows_before[miny]

        return t

    def Part2(self) -> BaseSolution.ResultType:
        universe = self.dataRaw.splitlines()
        height, width = len(universe), len(universe[0])

        galaxies = []
        empty_cols = [True for _ in range(width)]
        empty_rows = [True for _ in range(height)]

        for y in range(height):
            for x in range(width):
                if universe[y][x] == '#':
                    empty_cols[x] = False
                    empty_rows[y] = False
                    galaxies.append((x, y))

        empty_cols_before = [0 for _ in range(width + 1)]
        for x in range(width):
            empty_cols_before[x + 1] = empty_cols_before[x] + empty_cols[x]

        empty_rows_before = [0 for _ in range(height + 1)]
        for y in range(height):
            empty_rows_before[y + 1] = empty_rows_before[y] + empty_rows[y]

        t = 0
        n = len(galaxies)
        for i in range(n - 1):
            g1 = galaxies[i]

            for j in range(i + 1, n):
                g2 = galaxies[j]

                minx, maxx = min(g1[0], g2[0]), max(g1[0], g2[0])
                miny, maxy = min(g1[1], g2[1]), max(g1[1], g2[1])

                t += maxx - minx + maxy - miny
                t += (
                    empty_cols_before[maxx] - empty_cols_before[minx]
                    + empty_rows_before[maxy] - empty_rows_before[miny]
                ) * 999_999

        return t
