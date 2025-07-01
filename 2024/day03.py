from common.base_solution import BaseSolution
import re

class Solution(BaseSolution):
    def Part1(self) -> BaseSolution.ResultType:
        total = 0

        for match in re.findall(r"mul\(\d+,\d+\)", self.dataRaw):
            n1, n2 = map(int, re.findall(r"\d+", match))
            total += n1 * n2

        return total

    def Part2(self) -> BaseSolution.ResultType:
        total = 0

        do = True
        for match in re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", self.dataRaw):
            if match == "do()":
                do = True

            elif match == "don't()":
                do = False

            elif do:
                n1, n2 = map(int, re.findall(r"\d+", match))
                total += n1 * n2

        return total
