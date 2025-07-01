from common.base_solution import BaseSolution

class Solution(BaseSolution):
    def Part1(self) -> BaseSolution.ResultType:
        times = []
        records = []

        for line in self.dataRaw.splitlines():
            if line.startswith("Time:"):
                times = list(map(int, line.split(':')[1].strip().split()))
            else:
                records = list(map(int, line.split(':')[1].strip().split()))

        t = 1
        for i in range(len(times)):
            time = times[i]
            w = 0
            for j in range(time + 1):
                if (time - j) * j > records[i]:
                    w += 1
            t *= w

        return t

    def Part2(self) -> BaseSolution.ResultType:
        time = 0
        record = 0

        for line in self.dataRaw.splitlines():
            if line.startswith("Time:"):
                time = int("".join(line.split(':')[1].strip().split()))
            else:
                record = int("".join(line.split(':')[1].strip().split()))

        t = 0
        for j in range(time + 1):
            if (time - j) * j > record:
                t += 1

        return t
