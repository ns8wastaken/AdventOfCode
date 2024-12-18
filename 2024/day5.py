from common.base_solution import BaseSolution

class Solution(BaseSolution):
    def Part1(self) -> BaseSolution.ResultType:
        d1, d2 = self.dataRaw.split("\n\n")
        rules = [(int((s := i.split("|"))[0]), int(s[1])) for i in d1.split("\n")]
        data = [list(map(int, i.split(","))) for i in d2.split("\n")]

        total = 0

        for line in data:
            idx = {j: i for i, j in enumerate(line)}

            good = True
            for a, b in rules:
                if (a in idx) and (b in idx) and (idx[b] < idx[a]):
                    good = False
                    break

            if good:
                total += line[len(line) // 2]


        return total

    def Part2(self) -> BaseSolution.ResultType:
        d1, d2 = self.dataRaw.split("\n\n")
        rules = [(int((s := i.split("|"))[0]), int(s[1])) for i in d1.split("\n")]
        data = [list(map(int, i.split(","))) for i in d2.split("\n")]

        total = 0

        for line in data:
            idx = {j: i for i, j in enumerate(line)}

            good = True
            for a, b in rules:
                if (a in idx) and (b in idx) and (idx[b] < idx[a]):
                    good = False
                    break

            if not good:
                changesMade = True

                while changesMade:
                    changesMade = False
                    idx = {j: i for i, j in enumerate(line)}

                    for a, b in rules:
                        if (a in idx) and (b in idx) and (idx[b] < idx[a]):
                            line[idx[a]], line[idx[b]] = line[idx[b]], line[idx[a]]
                            changesMade = True
                            break

                total += line[len(line) // 2]

        return total
