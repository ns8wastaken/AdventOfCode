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

        shortest_num_len = len(min(d.keys(), key=lambda x: len(x)))
        longest_num_len = len(max(d.keys(), key=lambda x: len(x)))

        for line in self.dataRaw.splitlines():
            d1 = 0
            d2 = 0

            for i in range(len(line) - shortest_num_len + 1):
                if line[i].isdigit():
                    d1 = int(line[i])
                    break

                for j in range(longest_num_len, shortest_num_len - 1, -1):
                    w = line[i:i+j]
                    if w in d:
                        d1 = d[w]
                        break

                if d1 != 0:
                    break

            for i in range(len(line) - 1, -1, -1):
                if line[i].isdigit():
                    d2 = int(line[i])
                    break

                for j in range(longest_num_len, shortest_num_len - 1, -1):
                    w = line[i:i+j]
                    if w in d:
                        d2 = d[w]
                        break

                if d2 != 0:
                    break

            t += d1*10 + d2

        # return t
        return NotImplemented
