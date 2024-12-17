from common.base_solution import BaseSolution

class Solution(BaseSolution):
    def Part1(self) -> BaseSolution.ResultType:
        l = []

        for i in range(len(self.dataRaw)):
            if i % 2 == 0:
                for _ in range(int(self.dataRaw[i])):
                    l.append(str(i // 2))

            else:
                for _ in range(int(self.dataRaw[i])):
                    l.append(".")

        i = l.index(".")
        j = len(l) - 1

        while True:
            if l[j] == ".":
                j -= 1

            else:
                if j < i:
                    break

                l[i] = l[j]
                i = l.index(".", i + 1)
                j -= 1

        total = 0

        for i, s in enumerate(l[:j + 1]):
            total += i * int(s)

        return total

    def Part2(self) -> BaseSolution.ResultType:
        pass
