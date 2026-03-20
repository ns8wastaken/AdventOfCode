from common.base_solution import BaseSolution

class Solution(BaseSolution):
    def Part1(self) -> BaseSolution.ResultType:
        t = 0

        for joltages in self.dataRaw.splitlines():
            m = 0
            for i in range(len(joltages) - 1):
                for j in range(i + 1, len(joltages)):
                    n = int(f"{joltages[i]}{joltages[j]}")
                    if n > m:
                        m = n
            t += m

        return t

    def Part2(self) -> BaseSolution.ResultType:
        t = 0

        for joltages in self.dataRaw.splitlines():
            jolts = list(map(int, joltages))

            s = ""
            start = 0
            end = len(jolts) - 11

            for _ in range(12):
                m_i = start
                m = jolts[start]

                for i in range(start, end):
                    n = jolts[i]
                    if n > m:
                        m = n
                        m_i = i

                start = m_i + 1
                end += 1
                s += str(m)

            t += int(s)

        return t
