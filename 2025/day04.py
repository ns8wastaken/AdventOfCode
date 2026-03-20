from common.base_solution import BaseSolution
from utils.str2mat import str2mat

class Solution(BaseSolution):
    NEIGHBORS = (
        (-1, -1), (0, -1), (1, -1),
        (-1,  0),          (1,  0),
        (-1,  1), (0,  1), (1,  1),
    )

    def Part1(self) -> BaseSolution.ResultType:
        data = str2mat(self.dataRaw)

        h = len(data)
        w = len(data[0])

        t = 0

        for y in range(h):
            for x in range(w):
                if data[y][x] != '@':
                    continue

                c = 0

                for dx, dy in self.NEIGHBORS:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < w and 0 <= ny < h:
                        c += data[ny][nx] == '@'

                if c < 4:
                    t += 1

        return t

    def Part2(self) -> BaseSolution.ResultType:
        data = str2mat(self.dataRaw)

        h = len(data)
        w = len(data[0])

        t = 0

        done = False
        while not done:
            done = True

            d = data.copy()

            for y in range(h):
                for x in range(w):
                    if data[y][x] != '@':
                        continue

                    c = 0

                    for dx, dy in self.NEIGHBORS:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < w and 0 <= ny < h:
                            c += data[ny][nx] == '@'

                    if c < 4:
                        t += 1
                        done = False
                        d[y][x] = '.'

            data = d

        return t
