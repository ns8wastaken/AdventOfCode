from common.base_solution import BaseSolution

class Solution(BaseSolution):
    def Part1(self) -> BaseSolution.ResultType:
        t = 0

        for line in self.dataRaw.splitlines():
            vals = list(map(int, line.split()))
            iters = [vals]

            while any(vals):
                iters.append([])
                for i in range(len(vals) - 1):
                    iters[-1].append(vals[i + 1] - vals[i])
                vals = iters[-1]

            c = 0
            for i in reversed(iters):
                c += i[-1]
            t += c

        return t

    def Part2(self) -> BaseSolution.ResultType:
        t = 0

        for line in self.dataRaw.splitlines():
            vals = list(map(int, line.split()))
            iters = [vals]

            while any(vals):
                iters.append([])
                for i in range(len(vals) - 1):
                    iters[-1].append(vals[i + 1] - vals[i])
                vals = iters[-1]

            c = 0
            for i in reversed(iters):
                c = i[0] - c
            t += c

        return t
