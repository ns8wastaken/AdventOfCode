from common.base_solution import BaseSolution
import re

class Solution(BaseSolution):
    def Part1(self) -> BaseSolution.ResultType:
        data = [[list(map(int, re.findall(r"\d+", line))) for line in block.split("\n")] for block in self.dataRaw.split("\n\n")]

        total = 0

        for instructions in data:
            validOperations: list[tuple[int, int]] = []

            for a in range(100):
                for b in range(100):
                    if (a * instructions[0][0] + b * instructions[1][0] == instructions[2][0]) and (a * instructions[0][1] + b * instructions[1][1] == instructions[2][1]):
                        validOperations.append((a, b))

            if len(validOperations) == 0:
                continue

            validOperations.sort(key=lambda x: x[0] * 3 + x[1])
            total += validOperations[0][0] * 3 + validOperations[0][1]

        return total

    def Part2(self) -> BaseSolution.ResultType:
        data = [[list(map(int, re.findall(r"\d+", line))) for line in block.split("\n")] for block in self.dataRaw.split("\n\n")]
        for i in range(len(data)):
            data[i][2][0] += 10000000000000
            data[i][2][1] += 10000000000000

        total = 0

        for instructions in data:
            # a = (r1 - x2*((x1*r2 - y1*r1) / (x1*y2 - y1*x2))) / x1
            # b = (x1*r2 - y1*r1) / (x1*y2 - y1*x2)
            a = (instructions[2][0] - instructions[1][0] * ((instructions[0][0] * instructions[2][1] - instructions[0][1] * instructions[2][0]) / (instructions[0][0] * instructions[1][1] - instructions[0][1] * instructions[1][0]))) / instructions[0][0]
            b = (instructions[0][0] * instructions[2][1] - instructions[0][1] * instructions[2][0]) / (instructions[0][0] * instructions[1][1] - instructions[0][1] * instructions[1][0])

            if a != int(a) or b != int(b):
                continue

            total += int(a) * 3 + int(b)

        return total
