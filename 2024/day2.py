from common.base_solution import BaseSolution

def isSafe(l: list[int]) -> bool:
    increasing = (l[0] < l[1])
    decreasing = (not increasing)

    for i in range(1, len(l)):
        if increasing and (not (l[i] > l[i - 1])):
            return False

        elif decreasing and (not (l[i] < l[i - 1])):
            return False

        if (abs(l[i] - l[i - 1]) > 3) or (abs(l[i] - l[i - 1]) < 1):
            return False

    return True


class Solution(BaseSolution):
    def Part1(self) -> int:
        total = 0

        for line in self.dataRaw.split("\n"):
            total += isSafe([int(i) for i in line.split(" ")])

        return total

    def Part2(self) -> int:
        total = 0

        for line in self.dataRaw.split("\n"):
            l = [int(i) for i in line.split(" ")]

            safe = isSafe(l)

            if not safe:
                safe = any(isSafe([l[j] for j in range(len(l)) if j != i]) for i in range(len(l)))

            total += safe

        return total
