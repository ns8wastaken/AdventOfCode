from common.base_solution import BaseSolution

class Solution(BaseSolution):
    def Part1(self) -> BaseSolution.ResultType:
        beam = {self.dataRaw.index('S')}

        t = 0

        for l in self.dataRaw.splitlines():
            idx = []

            for i, c in enumerate(l):
                if c == '^':
                    idx.append(i)

            for i in idx:
                if i in beam:
                    beam.remove(i)
                    beam.add(i - 1)
                    beam.add(i + 1)
                    t += 1

        return t

    def Part2(self) -> BaseSolution.ResultType:
        return NotImplemented
