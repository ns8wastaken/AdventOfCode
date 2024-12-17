from common.base_solution import BaseSolution

class Solution(BaseSolution):
    def Part1(self) -> BaseSolution.ResultType:
        l1 = []
        l2 = []

        for i in self.dataRaw.split("\n"):
            l1.append(int(i[:5]))
            l2.append(int(i[8:]))

        l1.sort()
        l2.sort()

        total = 0

        for i in range(len(l1)):
            total += abs(l1[i] - l2[i])

        return total

    def Part2(self) -> BaseSolution.ResultType:
        l1 = set()
        l2 = []

        for i in self.dataRaw.split("\n"):
            l1.add(int(i[:5]))
            l2.append(int(i[8:]))

        l1_list = list(l1)
        l1_list.sort()

        total = 0

        for i in l1_list:
            total += i * l2.count(i)

        return total
