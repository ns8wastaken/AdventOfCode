from common.base_solution import BaseSolution
import sys
from collections import Counter

class Solution(BaseSolution):
    def Part1(self) -> BaseSolution.ResultType:
        l = list(map(int, self.dataRaw.split(" ")))

        for _ in range(25):
            temp = []

            for i in range(len(l)):
                s = str(l[i])

                if l[i] == 0:
                    temp.append(1)

                elif len(s) % 2 == 0:
                    mid = len(s) // 2
                    temp.append(int(s[:mid]))
                    temp.append(int(s[mid:]))

                else:
                    temp.append(l[i] * 2024)

            l = temp

        return len(l)

    def Part2(self) -> BaseSolution.ResultType:
        def change(stone: int):
            if stone == 0:
                yield 1

            else:
                digits = str(stone)

                if len(digits) % 2:
                    yield stone * 2024

                else:
                    mid = len(digits) // 2
                    yield int(digits[:mid])
                    yield int(digits[mid:])

        stones = Counter(map(int, self.dataRaw.split(" ")))

        for _ in range(75):
            new = Counter()

            for stone, occurrences in stones.items():
                for newstone in change(stone):
                    new[newstone] += occurrences

            stones = new

        return sum(stones.values())
