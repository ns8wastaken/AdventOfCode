from common.base_solution import BaseSolution

class Solution(BaseSolution):
    def Part1(self) -> BaseSolution.ResultType:
        t = 0
        d = 50
        for l in self.dataRaw.splitlines():
            n = -1 if l[0] == 'L' else 1
            d = (d + n * int(l[1:])) % 100
            t += d == 0
        return t

    def Part2(self) -> BaseSolution.ResultType:
        t = 0
        d = 50
        for l in self.dataRaw.splitlines():
            n = -1 if l[0] == 'L' else 1
            d = (d + n * int(l[1:])) % 100
            t += d == 0
        return t
