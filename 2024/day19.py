from common.base_solution import BaseSolution

class Solution(BaseSolution):
    def Part1(self) -> BaseSolution.ResultType:
        data_split = self.dataRaw.split("\n\n")

        patterns = data_split[0].strip().split(", ")
        designs = data_split[1].strip().split('\n')

        cache = dict()
        def solve(d: str) -> int:
            if d not in cache:
                if len(d) == 0:
                    return True

                else:
                    r = False
                    for p in patterns:
                        if d.startswith(p):
                            r |= solve(d[len(p):])
                    cache[d] = r

            return cache[d]

        return sum(solve(d) for d in designs)

    def Part2(self) -> BaseSolution.ResultType:
        data_split = self.dataRaw.split("\n\n")

        patterns = data_split[0].strip().split(", ")
        designs = data_split[1].strip().split('\n')

        cache = dict()
        def solve(d: str) -> int:
            if d not in cache:
                if len(d) == 0:
                    return 1

                else:
                    r = 0
                    for p in patterns:
                        if d.startswith(p):
                            r += solve(d[len(p):])
                    cache[d] = r

            return cache[d]

        return sum(solve(d) for d in designs)
