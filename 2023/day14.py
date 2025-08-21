from common.base_solution import BaseSolution

class Solution(BaseSolution):
    def Part1(self) -> BaseSolution.ResultType:
        data = self.dataRaw.splitlines()

        list_zippy = lambda m: list(map(list, zip(*m)))

        z = list_zippy(data)

        for col in z:
            y = 0
            for curr in range(len(col)):
                c = col[curr]

                match c:
                    case '#':
                        y = curr + 1

                    case 'O':
                        col[curr] = '.'
                        col[y] = 'O'
                        y += 1

        t = 0

        zz = list_zippy(z)
        for y, row in enumerate(zz):
            n = 0
            for c in row:
                if c == 'O':
                    n += 1
            t += (len(zz) - y) * n

        return t

    def Part2(self) -> BaseSolution.ResultType:
        # The pattern repeats at some point so just calculate the final restult based on that
        return NotImplemented
