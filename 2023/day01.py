from common.base_solution import BaseSolution

class Solution(BaseSolution):
    def Part1(self) -> BaseSolution.ResultType:
        t = 0

        for line in self.dataRaw.splitlines():
            d1 = ''
            d2 = ''

            for c in line:
                if c.isdigit():
                    d1 = c
                    break

            for i in range(len(line) - 1, -1, -1):
                if line[i].isdigit():
                    d2 = line[i]
                    break

            t += int(d1 + d2)

        return t

    def Part2(self) -> BaseSolution.ResultType:
        d = {
            "one":   1,
            "two":   2,
            "three": 3,
            "four":  4,
            "five":  5,
            "six":   6,
            "seven": 7,
            "eight": 8,
            "nine":  9,
            "ten":   10
        }

        t = 0

        longest_num_len = len(max(d.keys(), key=lambda x: len(x)))

        for line in self.dataRaw.splitlines():
            d1 = -1

            for i in range(len(line)):
                gucci = False

                if line[i].isdigit():
                    d1 = int(line[i])
                    break

                for j in range(i + 1, i + 1 + longest_num_len):
                    if j > len(line):
                        break

                    if (n := line[i:j]) in d:
                        d1 = d[n]
                        gucci = True
                        break

                if gucci:
                    break

            if d1 == -1:
                raise RuntimeError("Ruh roh")

            d2 = -1

            for i in range(len(line) - 1, -1, -1):
                gucci = False

                if line[i].isdigit():
                    d2 = int(line[i])
                    break

                for j in range(i + 1, i + 1 + longest_num_len):
                    if j > len(line):
                        break

                    if (n := line[i:j]) in d:
                        d2 = d[n]
                        gucci = True
                        break

                if gucci:
                    break

            if d2 == -1:
                raise RuntimeError("Ruh roh")

            t += int(f"{d1}{d2}")

        return t
