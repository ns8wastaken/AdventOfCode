from common.base_solution import BaseSolution

class Solution(BaseSolution):
    def Part1(self) -> BaseSolution.ResultType:
        t = 0

        for data in self.dataRaw.split(','):
            start, end = map(int, data.split('-'))

            for n in range(start, end + 1):
                s = str(n)

                if len(s) % 2 != 0:
                    continue

                m = len(s) // 2

                if s[:m] == s[m:]:
                    t += int(s)

        return t

    def Part2(self) -> BaseSolution.ResultType:
        t = 0

        for data in self.dataRaw.split(','):
            start, end = map(int, data.split('-'))

            for n in range(start, end + 1):
                s = str(n)

                for i in range(1, len(s) // 2 + 1):
                    sub = s[:i]

                    if len(s) % len(sub) != 0:
                        continue

                    if s == sub * (len(s) // len(sub)):
                        t += int(s)
                        break
        return t
