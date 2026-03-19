from common.base_solution import BaseSolution
from functools import reduce

class Solution(BaseSolution):
    bigL = lambda x: len(x) > 0
    mul = lambda l: reduce(lambda x,y: x*y, l)
    fillSplit = lambda l: filter(Solution.bigL, l.split(' '))

    def Part1(self) -> BaseSolution.ResultType:
        *nums, ops = self.dataRaw.splitlines()

        cols = []
        for l in nums:
            for i, n_str in enumerate(Solution.fillSplit(l)):
                n = int(n_str)

                if len(cols) <= i:
                    cols.append([n])
                else:
                    cols[i].append(n)

        t = 0

        for i, o in enumerate(Solution.fillSplit(ops)):
            ns = cols[i]
            match o:
                case '+': t += sum(ns)
                case '*': t += reduce(lambda x,y: x*y, ns)

        return t

    def Part2(self) -> BaseSolution.ResultType:
        *nums, ops = self.dataRaw.splitlines()
        ops = list(Solution.fillSplit(ops))

        t = 0

        i = 0
        tmp = []
        for l in zip(*nums):
            n_str = "".join(l).strip()

            if len(n_str) == 0:
                match ops[i]:
                    case '+': t += sum(tmp)
                    case '*': t += Solution.mul(tmp)
                tmp.clear()
                i += 1
                continue

            tmp.append(int(n_str))

        match ops[-1]:
            case '+': t += sum(tmp)
            case '*': t += Solution.mul(tmp)

        return t
