from common.base_solution import BaseSolution

class Solution(BaseSolution):
    def Part1(self) -> BaseSolution.ResultType:
        data = [i.strip() for i in self.dataRaw.split("\n")]

        total = 0

        # Horizontal words
        for line in data:
            for i in range(len(line) - 3):
                s = line[i:i+4]
                if (s == "XMAS") or (s == "SAMX"):
                    total += 1

        # Vertical words
        for i in range(len(data) - 3):
            for j in range(len(data[i])):
                s = data[i][j] + data[i + 1][j] + data[i + 2][j] + data[i + 3][j]
                if (s == "XMAS") or (s == "SAMX"):
                    total += 1

        # Diagonals
        for i in range(len(data) - 3):
            for j in range(len(data[i]) - 3):
                s = data[i][j + 3] + data[i + 1][j + 2] + data[i + 2][j + 1] + data[i + 3][j]
                if (s == "XMAS") or (s == "SAMX"):
                    total += 1

                s = data[i][j] + data[i + 1][j + 1] + data[i + 2][j + 2] + data[i + 3][j + 3]
                if (s == "XMAS") or (s == "SAMX"):
                    total += 1

        return total

    def Part2(self) -> BaseSolution.ResultType:
        data = [i.strip() for i in self.dataRaw.split("\n")]

        total = 0

        for i in range(len(data) - 2):
            for j in range(len(data[i]) - 2):
                s1 = data[i][j] + data[i + 1][j + 1] + data[i + 2][j + 2]
                s2 = data[i + 2][j] + data[i + 1][j + 1] + data[i][j + 2]

                if ((s1 == "MAS") or (s1 == "SAM")) and ((s2 == "MAS") or (s2 == "SAM")):
                    total += 1

        return total
